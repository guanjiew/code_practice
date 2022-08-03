class MyCalendar {
    TreeMap<Integer, Integer> calendar;

    public MyCalendar() {
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
// Space complexity: O(