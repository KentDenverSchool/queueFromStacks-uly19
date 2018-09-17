# QueueFromStacks
A Queue can be simulated using two Stacks: One for **enqueuing** and one for **dequeuing**

When you dequeue and the dequeuing stack is empty, transfer all enqueue stack items onto the dequeueing stack using pop and push (thus reversing order of elements as they enter the dequeuing stack).

```java

void enqueue(E element)    //add an element
E dequeue()                //remove and return the least recent element
boolean isEmpty()   
int size()

//not required, but common
E peek()                //look at the least recent element without removing

```


### Your Assignment

Complete the class `StackQueue.java`. You may only use two Stack objects as instance data. **Write the best case, worst case and average case runtime of dequeue() above the method.** Test that it works by writing a driver.
