// https://leetcode.com/problems/my-calendar-i/
// Condition for calendar overlap:
// Not (start1 > end2 || start2 > end1) = (start1 <= end2 && start2 <= end1)


class CalendarList {
    ArrayList<int[]> calendar;

    public CalendarList() {
        calendar = new ArrayList<>();
    }
    
    public boolean book(int start, int end) {
        for (int[] c: calendar) {
            if (c[0] < end && c[1] > start)
                return false;
        }
        calendar.add(new int[]{start, end});
    }

    public void print() {
        for (int[] c: calendar) {
            System.out.println(c[0] + " " + c[1]);
        }
    }
}
// To process n calendars
// Space complexity: O(n)
// Time complexity: O(n^2)


// Use a balanced binary search tree to store the calendars
// Use a TreeMap to store the calendars

class CalendarTreeMap {
    TreeMap<Integer, Integer> calendar;

    public CalendarTreeMap() {
        calendar = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);
        if (prev != null && calendar.get(prev) > start) {
            return false;
        }
        Integer next = calendar.ceilingKey(start);
        if (next != null && next < end) {
            return false;
        }
        calendar.put(start, end);
        return true;
    }
}

// Runtime complexity: O(log(n))
// Space complexity: O(n)

