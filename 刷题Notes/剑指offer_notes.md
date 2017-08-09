1. 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

   ```java
   public class Solution {
       public String replaceSpace(StringBuffer str) {
           int numOfSpace = 0;
           for (int i = 0; i < str.length(); i++){
               if (str.charAt(i) == ' '){
                   numOfSpace++;
               }
           }
           int newLength = str.length() + numOfSpace * 2;
           int theIndexOriginal = str.length() - 1;
           int theIndexFinal = newLength - 1;
           str.setLength(newLength);
           for (; theIndexOriginal >= 0 && theIndexOriginal<newLength ; --theIndexOriginal) {
               if (str.charAt(theIndexOriginal) == ' ') {
                   str.setCharAt(theIndexFinal--, '0');
                   str.setCharAt(theIndexFinal--, '2');
                   str.setCharAt(theIndexFinal--, '%');
               } else {
                   str.setCharAt(theIndexFinal--, str.charAt(theIndexOriginal));
               }
           }
           return str.toString();
       }
   }
   ```

2. 输入一个链表，从尾到头打印链表每个节点的值。

   ```java
   import java.util.ArrayList;
   public class Solution {
       ArrayList<Integer> result = new ArrayList<Integer>();
       public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
           if(listNode != null){
               this.printListFromTailToHead(listNode.next);
               result.add(listNode.val);
           }
           return result;
       }
   }
   ```

3. 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

   ```java
   import java.util.Stack;

   public class Solution {
       Stack<Integer> stack1 = new Stack<Integer>();
       Stack<Integer> stack2 = new Stack<Integer>();
       
       public void push(int node) {
           stack1.push(node);
       }
       
       public int pop() {
           if (stack2.isEmpty()){
               while(!stack1.isEmpty()){
                   stack2.push(stack1.pop());
               }
           }
           return stack2.pop();
       }
   }
   ```

4. 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

   ```java
   import java.util.ArrayList;
   public class Solution {
       public int minNumberInRotateArray(int [] array) {
           int low = 0 ; int high = array.length - 1;
           while(low < high){
               int mid = low + (high - low) / 2;
               if(array[mid] > array[high]){
                   low = mid + 1;
               }else if(array[mid] == array[high]){
                   high = high - 1;
               }else{
                   high = mid;
               }
           }
           return array[low];
       }
   } // 考虑了类似{1，1，1，0，1，1}的特殊情况
   ```

5. 斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。

   ```java
   public class Solution {
       public int Fibonacci(int n) {
           if (n == 0) {
               return 0;
           } 
           if (n == 1) {
               return 1;
           }
           
           int result = 0;
           int preNum = 1;
           int prePreNum = 0;
           
           for (int i = 2; i <= n; i++){
               result = preNum + prePreNum;
               prePreNum = preNum;
               preNum = result;
           }
           return result;
       }
   }
   ```

6. 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

   ```java
   public class Solution {
     // a.如果两种跳法，1阶或者2阶，那么假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1);
     // b.假定第一次跳的是2阶，那么剩下的是n-2个台阶，跳法是f(n-2) 
     // c.由a\b假设可以得出总跳法为: f(n) = f(n-1) + f(n-2)
     // d.然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
     // e.可以发现最终得出的是一个斐波那契数列：
       public int JumpFloor(int target) {
           if (target == 1) {
               return 1;
           } 
           if (target == 2) {
               return 2;
           }
           
           int result = 0;
           int preNum = 2;
           int prePreNum = 1;
           
           for (int i = 3; i <= target; i++){
               result = preNum + prePreNum;
               prePreNum = preNum;
               preNum = result;
           }
           return result;
       }
   }
   ```

7. 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

   ```java
   public class Solution {
     	// 因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
   	// 跳1级，剩下n-1级，则剩下跳法是f(n-1)
   	// 跳2级，剩下n-2级，则剩下跳法是f(n-2)
   	// 所以f(n)=f(n-1)+f(n-2)+...+f(1)
   	// 因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
   	// 所以f(n)=2*f(n-1)
       public int JumpFloorII(int target) {
           if (target <= 0){
               return 0;
           }
           if (target == 1){
               return 1;
           }else {
               return 2 * JumpFloorII(target - 1);
           }
       }
   }
   ```

8. 我们可以用2 \*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2\*1的小矩形无重叠地覆盖一个2\*n的大矩形，总共有多少种方法？

   ```java
   public class Solution {
       public int RectCover(int target) {
           if (target < 1){
               return 0;
           } else if (target == 1 || target == 2) {
               return target;
           } else {
               return RectCover(target -1) + RectCover(target - 2);
           }
       }
   }
   ```

9. 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

   ```java
   public class Solution {
       public int NumberOf1(int n) {
           int count = 0;
           while (n != 0) {
               count++;
               n = n & (n - 1);
           }
           return count;
       }
   }
   ```

10. 给定一个double类型的浮点数base和int类型的整数exponent，求base的exponent次方。

   ```java
   public class Solution {
       public double Power(double base, int exponent) {
           double res = 1; // 注意定义的数据类型，如果是int会返回0
           
           if (base == 0 && exponent < 0){
             	// 考虑base是0，而exp是负数的情况，这里，0不能为分母
               throw new RuntimeException("分母不能为0");
           }
           
           for (int i = 0; i < Math.abs(exponent); i++){
               res *= base;
           }
           
         	// 考虑exp是正还是负数的情况，决定返回的值是分数or what
           if (exponent < 0) {
               return 1 / res;
           } else {
               return res;
           }
     }
   }
   ```

11. 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

    ```java
    public class Solution {
        public void reOrderArray(int [] array) {
            int len = array.length;
            int[] res = new int[len];
            
            int oddIndex = 0;
            int oddNum = 0;
            
            for (int i = 0; i < len; i++){
                if (isOdd(array[i])) {
                    oddNum++;
                }
            }
            
            for (int i = 0; i < len; i++) {
                if (isOdd(array[i])) {
                    res[oddIndex++] = array[i];
                } else {
                    res[oddNum++] = array[i];
                }
            }
            
            for (int i = 0; i < len; i++){
                array[i] = res[i];
            }
            
        }
        
        public boolean isOdd(int n) {
            if ((n % 2) == 0){
                return false;
            } else {
                return true;
            }
        }
    }
    ```

12. ​