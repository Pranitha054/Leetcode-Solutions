import java.util.Stack;

class MinStack {

    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }

    public void pop() {
        int removed = stack.pop();
        if (removed == minStack.peek()) {
            minStack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Example usage:
 * MinStack obj = new MinStack();
 * obj.push(-2);
 * obj.push(0);
 * obj.push(-3);
 * int min1 = obj.getMin();  // returns -3
 * obj.pop();
 * int top = obj.top();      // returns 0
 * int min2 = obj.getMin();  // returns -2
 */
