from multiprocessing import Process
import time
from itertools import count

SELECTS = ["TOP-LEFT-SELECT", "TOP-RIGHT-SELECT", "BOTTOM-LEFT-SELECT", "BOTTOM-RIGHT-SELECT"]
MINUS = "CENTRE-MINUS"
POWER = "POWER-BUTTON"
POWER_TIMEOUT = 20
SELECT_TIMEOUT = 10


class FulgorMilanoCooktop:

    def __init__(self):
        self.select_controls = SELECTS
        self.minus_control = MINUS
        self.power = POWER
        self.is_locked = False
        self.is_temp_locked = False
        self.is_on = False
        self.displays = [None] * 4

    def print_display(self, error=False):
        if self.is_on:
            if self.is_locked:
                self.displays = ['L'] * 4
            else:
                self.displays = ['0'] * 4
            if self.is_locked and not self.is_temp_locked:
                self.displays = ['0'] * 4
            if error:
                self.displays = ['E', 'R', '0', '3']

        print("***********")
        print(self.displays[0], " S-", " S-", self.displays[1])
        print('     -     ')
        print(self.displays[2], " S-", " S-", self.displays[3])
        print("***********")

    def hold_buttons(self, buttons, interval=1):
        timeout_start = time.time()
        print("Operate {} buttons for {} seconds".format(" AND ".join(buttons), interval))
        counter = count(1)

        while self.is_on and time.time() < timeout_start + interval:
            print("Holding for {} seconds".format(next(counter)))
            time.sleep(1)
        print("\n")
        return 0

    def timeout_helper(self, process, p_name):
        p1 = Process(target=process, args=(self,), name=p_name)
        p1.start()
        p1.join(timeout=min(SELECT_TIMEOUT, POWER_TIMEOUT))
        p1.terminate()
        return p1

    def turn_on(self):
        print("Turn On Stove!")
        if not self.is_on:
            self.hold_buttons([self.power])
            if not self.is_locked:
                self.displays = [0] * 4
            self.is_on = True
        self.print_display()

    def lock(self, lock_operations):
        self.turn_on()
        if self.is_on:
            p1 = self.timeout_helper(lock_operations, "Lock")
            if p1.exitcode is None:
                self.print_display(error=True)
                print(
                    "Timeout Error: The above steps have been carried out exceeding {} seconds".format(SELECT_TIMEOUT))
            else:
                self.is_locked = True
                self.is_temp_locked = True
                self.print_display()
                print("Successfully Locked!")

    def unlock_temp(self, unlock_operations):
        self.turn_on()
        if self.is_on and self.is_locked:
            p1 = self.timeout_helper(unlock_operations, "Unlocking Temp")
            if p1.exitcode is None:
                self.print_display()
                print(
                    "Timeout Error: The above steps have been carried out exceeding {} seconds".format(SELECT_TIMEOUT))
            else:
                self.is_temp_locked = False
                self.print_display(error=True)
                print("Successfully Unlocked temporality!")
                self.is_locked = True
                self.is_temp_locked = True

    def unlock_perm(self, unlock_operations):
        self.turn_on()
        if self.is_on and self.is_locked:
            p1 = self.timeout_helper(unlock_operations, "Unlocking")
            if p1.exitcode is None:
                self.print_display(error=True)
                print(
                    "Timeout Error: The above steps have been carried out exceeding {} seconds".format(SELECT_TIMEOUT))
            else:
                self.is_temp_locked = False
                self.is_locked = False
                self.print_display()
                print("Successfully Unlocked Permanently!")


def operate_lock(cooktop):
    cooktop.hold_buttons([cooktop.select_controls[3], cooktop.minus_control], 2)
    cooktop.hold_buttons([cooktop.select_controls[3]])


def operate_unlock_temp(cooktop):
    cooktop.hold_buttons([cooktop.select_controls[3], cooktop.minus_control], 2)


def operate_unlock_perm(cooktop):
    cooktop.hold_buttons([cooktop.select_controls[3], cooktop.minus_control], 2)
    cooktop.hold_buttons([cooktop.minus_control])


if __name__ == '__main__':
    my_cooktop = FulgorMilanoCooktop()
    print("Simulation for locking the stove:")
    my_cooktop.lock(operate_lock)
    print("\n")
    print("Simulation for unlocking the stove temporality for cooking")
    my_cooktop.unlock_temp(operate_unlock_temp)
    print("If I turn on the stove, it is still locked")
    my_cooktop.print_display()
    print("\n")
    print("Simulation for unlocking the stove permanently ")
    my_cooktop.unlock_perm(operate_unlock_perm)
