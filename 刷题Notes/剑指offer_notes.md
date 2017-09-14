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

12. 输入一个链表，反转链表后，输出链表的所有元素。

    ```java
    public class Solution {
        public ListNode ReverseList(ListNode head) {
          	// 首先，是对异常情况的处理，如果输入为空，那么返回空
            if (head == null) {
                return null;
            }
          	// 定义head节点的pre和next节点，先初始化为空
            ListNode pre = null;
            ListNode next = null;
            
          	// 循环操作，直至当前节点为空
            while (head != null) {
              	// 先将当前节点的写一个节点存储在next中
                next = head.next;
              	// 将当前节点的下个节点设置为当前节点的前一个节点，以达到反转的目的
                head.next = pre;
              	// 因为要一直进行下去，则将pre这个节点的值，设定为head，在下一次执行上一步赋值操作的时候，将下一个节点的前一个节点设置为当前节点
                pre = head;
              	// 这里就是将当前节点设置为下一个节点，即往链表的下一个节点推进了一步
                head = next;
            }
            // 跳出循环的时候，当前节点已经为空，所以应该返回的是当前节点的前一个节点，即pre
            return pre;
        }
    }
    ```

13. 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

    ```java
    // 递归版本
    public class Solution {
        public ListNode Merge(ListNode list1,ListNode list2) {
            if (list1 == null) {
                return list2;
            }
            
            if (list2 == null) {
                return list1;
            }
            
            if (list1.val <= list2.val) {
                list1.next = Merge(list1.next, list2);
                return list1;
            } else {
                list2.next = Merge(list1, list2.next);
                return list2;
            }
        }
    }

    // 非递归版本
    public class Solution {
        public ListNode Merge(ListNode list1,ListNode list2) {
          	// 异常情况处理，如果两个list中有一个是空，则返回另一个list
            if (list1 == null) {
                return list2;
            }
            if (list2 == null) {
                return list1;
            }
            
          	// 定义要返回的结果和当前节点
            ListNode res = null;
            ListNode current = null;
            
          	// 在两个list都不为空的情况下，进行val的对比
            while (list1 != null && list2 != null) {
                if (list1.val <= list2.val) {
                    if (res == null) {
                      	// 如果当前res为空，则说明刚刚开始循环，将头节点设置为res
                        res = current = list1;
                    } else {
                      	// 否则，在之后添加next
                        current.next = list1;
                        current = current.next;
                    }
                    list1 = list1.next;
                } else {
                    if (res == null) {
                        res = current = list2;
                    } else {
                        current.next = list2;
                        current = current.next;
                    }
                    list2 = list2.next;
                }
            }
            
          	// 找到跳出循环的原因，如果是list1先为空，那么直接将list2添加在res后面即可，否则添加list1
            if (list1 == null) {
                current.next = list2;
            } else {
                current.next = list1;
            }
            
            return res;
        }
    }
    ```

14. 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

    ```java
    public class Solution {
        public boolean HasSubtree(TreeNode root1,TreeNode root2) {
            if (root2 == null) {
                return false;
            }
            
            if (root1 == null) {
                return false;
            }
            
            boolean flag = false;
            
            if (root1.val == root2.val) {
                flag = isSubTree(root1, root2);
            }
            
            if (!flag) {
                flag = HasSubtree(root1.left, root2);
                if (!flag) {
                    flag = HasSubtree(root1.right, root2);
                }
            }
            
            return flag;
        }
        
        private boolean isSubTree(TreeNode r1, TreeNode r2) {
            if (r2 == null) {
                return true;
            }
            
            if (r1 == null) {
                return false;
            }
            
            if (r1.val != r2.val) {
                return false;
            }
            return isSubTree(r1.left, r2.left) && isSubTree(r1.right, r2.right);
        }
    }
    ```

15. 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

    ```java
    import java.util.ArrayList;
    public class Solution {
        public ArrayList<Integer> printMatrix(int [][] matrix) {
           ArrayList<Integer> res = new ArrayList<>();
            
            int n = matrix.length;
            int m = matrix[0].length;
            
            if (m == 0 || n == 0) {
                return null;
            }
            
            int layers = (Math.min(n, m) - 1) / 2 + 1;
            for(int i=0; i < layers; i++){
                
                for(int k = i; k < m - i; k++) {
                    res.add(matrix[i][k]);
                }
                for(int j = i + 1; j < n - i; j++) {
                    res.add(matrix[j][m - i - 1]);
                }
                for(int k = m - i - 2; (k >= i) && (n - i - 1 != i); k--) {
                    res.add(matrix[n - i - 1][k]);
                }
                for(int j = n - i - 2;(j > i) && (m - i - 1 != i); j--) {
                    res.add(matrix[j][i]);
                }
            }
            
            return res;
        }
    }
    ```

16. 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

    ```java
    import java.util.Stack;

    public class Solution {

        Stack<Integer> data = new Stack<>();
        Stack<Integer> min = new Stack<>();
        
        Integer preAddNode = null;
        public void push(int node) {
            if (preAddNode != null) {
                if (node <= preAddNode) {
                    preAddNode = node;
                    min.push(node);
                }
                data.push(node);
            } else {
                preAddNode = node;
                data.push(node);
                min.push(node);
            }
        }
        
        public void pop() {
            int num1 = data.pop();
            int num2 = min.pop();
            if (num1 != num2) {
                min.push(num2);
            }
        }
        
        public int top() {
            int topNode = data.pop();
            data.push(topNode);
            return topNode;
        }
        
        public int min() {
            int minNode = min.pop();
            min.push(minNode);
            return minNode;
        }
    }
    ```

17. 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

    ```java
    /*
    public class RandomListNode {
        int label;
        RandomListNode next = null;
        RandomListNode random = null;

        RandomListNode(int label) {
            this.label = label;
        }
    }
    */
    public class Solution {
        public RandomListNode Clone(RandomListNode pHead)
        {
            if (pHead == null){
                return null;
            }
            RandomListNode pCur = pHead;
            
            while (pCur != null) {
                RandomListNode temp = new RandomListNode(pCur.label);
                temp.next = pCur.next;
                pCur.next = temp;
                pCur = temp.next;
            }
            pCur = pHead;
            
            while (pCur != null) {
                if (pCur.random != null) {
                    pCur.next.random = pCur.random.next;
                }
                pCur = pCur.next.next;
            }
            
            RandomListNode head = pHead.next;
            RandomListNode cur = head;
            pCur = pHead;
            while (pCur != null) {
                pCur.next = pCur.next.next;
                if (cur.next != null){
                    cur.next = cur.next.next;
                }
                pCur = pCur.next;
                cur = cur.next;
            }
            
            return head;
        }
    }
    ```

18. ​输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

    ```java
    // 1. 先序遍历的第一个位置一定是根节点 root
    // 2. 中序遍历的根节点位置在p，在p左边的节点都是root左子树的中序遍历数组，右边同理
    // 3. 先序遍历的第二个位置到p之间(闭区间)一定是root左子树的先序遍历，右边同理
    // 4. 四个数组摘出来，分左右递归
    public class Solution {
        public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
            TreeNode res = reCon(pre, 0, pre.length - 1, in, 0, in.length - 1);
            return res;
        }
        
        private TreeNode reCon(int[] pre, int preStart,int preEnd, 
                               int[] in, int inStart, int inEnd){
            if (preStart > preEnd || inStart > inEnd) {
                return null;
            }
            
            TreeNode root = new TreeNode(pre[preStart]);
            
            for (int i = inStart; i <= inEnd; i++ ){
                if (in[i] == pre[preStart]) {
                    root.left = reCon(pre, preStart + 1, preStart + i - inStart,
                                     in, inStart, i - 1);
                    root.right = reCon(pre, preStart + i + 1 - inStart, preEnd,
                                      in, i + 1, inEnd);
                }
            }
            return root;
        }
    }
    ```

19. 操作给定的二叉树，将其变换为源二叉树的镜像

    ```java
    // 先前序遍历这棵树的每个结点，如果遍历到的结点有子结点，就交换它的两个子节点，
    // 当交换完所有的非叶子结点的左右子结点之后，就得到了树的镜像
    // 递归的解法
    public class Solution {
        public void Mirror(TreeNode root) {
          // 最开始的base case
            if (root == null) {
                return;
            }
            
          // 运行中的base case，如果节点没有任何子节点，结束
            if (root.left == null && root.right == null) {
                return;
            }
           
          // 交换给定节点的左右子节点，如有一个为空也没有关系
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
            
          // 如果该节点有左或者右子节点，递归交换其左或者右子节点的，子代节点的位置
            if (root.left != null) {
                Mirror(root.left);
            }
            if (root.right != null) {
                Mirror(root.right);
            }
        }
    }
    ```

20. 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

    ```java
    /**
    【思路】借用一个辅助的栈，遍历压栈顺序，先讲第一个放入栈中，这里是1，然后判断栈顶元素是不是出栈顺序的第一个元素，这里是4，很显然1≠4，所以我们继续压栈，直到相等以后开始出栈，出栈一个元素，则将出栈顺序向后移动一位，直到不相等，这样循环等压栈顺序遍历完成，如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序。
    举例：
    入栈1,2,3,4,5
    出栈4,5,3,2,1
    首先1入辅助栈，此时栈顶1≠4，继续入栈2
    此时栈顶2≠4，继续入栈3
    此时栈顶3≠4，继续入栈4
    此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，,辅助栈里面是1,2,3
    此时栈顶3≠5，继续入栈5
    此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，,辅助栈里面是1,2,3
    ….
    依次执行，最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序。
    **/
    import java.util.Stack;

    public class Solution {
        public boolean IsPopOrder(int [] pushA,int [] popA) {
          // 若给定的数组为空，返回false
            if (pushA.length == 0 || popA.length == 0) {
                return false;
            }
          // 引入辅助栈用于判断
            Stack<Integer> s = new Stack<>();
          // popA的弹出index
            int index = 0;
            for (int i = 0; i < pushA.length; i++){
                s.push(pushA[i]);
                while (!s.empty() && s.peek() == popA[index]) {
                    s.pop(); // 辅助栈弹出
                    index++; // 弹出index自增
                }
            }
            return s.empty();
        }
    }
    ```

21.  从上往下打印出二叉树的每个节点，同层节点从左至右打印。 （所谓广度优先 BFS）

    ```java
    public class Solution {
        public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
            ArrayList<TreeNode> listNode = new ArrayList<>();
            ArrayList<Integer> listVal = new ArrayList<>();
            if (root == null) {
                return listVal;
            }
            listNode.add(root);
            listVal.add(root.val);
          // 此处，虽然一开始size为1， 但是在循环体的内部，随着需要，会扩大listNode的size，
          // 所以这里的循环会一直持续到遍历完所有的node为止
            for (int i = 0; i < listNode.size(); i++) {
                TreeNode node = listNode.get(i);
                if (node.left != null) {
                    listNode.add(node.left);
                    listVal.add(node.left.val);
                }
                if (node.right != null) {
                    listNode.add(node.right);
                    listVal.add(node.right.val);
                }
            }
            
            return listVal;
        }
    }
    ```

22. 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

    ```java
    public class Solution {
        public boolean VerifySquenceOfBST(int [] sequence) {
            if (sequence.length == 0 || sequence == null) {
                return false;
            }
            if (sequence.length == 1) {
                return true;
            }
            return verBST(sequence, 0, sequence.length - 1);
        }
        public boolean verBST(int[] a, int start, int end) {
            if (start >= end) {
                return true;
            }
            int i = end;
            while (i > start && a[i - 1] > a[end]) {
                i--;
            }
            for (int j = start; j < i - 1; j++) {
                if (a[j] > a[end]) {
                    return false;
                }
            }
            return verBST(a, start, i - 1) && verBST(a, i, end - 1);
        }
    }
    ```

23. 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

    ```java
    public class Solution {
        private ArrayList<ArrayList<Integer>> listAll = new ArrayList<ArrayList<Integer>>(); 
        private ArrayList<Integer> list = new ArrayList<Integer>(); 
        
        public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) { 
            if(root == null) {
                return listAll; 
            }
            
            list.add(root.val); 
            target -= root.val; 
            if(target == 0 && root.left == null && root.right == null) {
                listAll.add(new ArrayList<Integer>(list)); 
            }
            FindPath(root.left, target); 
            FindPath(root.right, target); 
            list.remove(list.size()-1); 
            return listAll; }
    }
    ```

24. 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

    ```java
    public class Solution {
      // 定义将要返回的存放路径的arraylist，每一条路径都以arraylist的形式存在，所以结果应该是一个集合的集合
        private ArrayList<ArrayList<Integer>> listAll = new ArrayList<>(); 
        private ArrayList<Integer> list = new ArrayList<>(); 
        
        public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) { 
          // 如果根节点是空，返回空的集合
            if(root == null) {
                return listAll; 
            }
            
            list.add(root.val); 
            target -= root.val; 
          // 满足条件的情况是，target为0，当前节点是leaf node，若以上为true，则添加该条路径
            if(target == 0 && root.left == null && root.right == null) {
                listAll.add(new ArrayList<Integer>(list)); 
            }
          // 递归进行同样的操作，此时的target已经是去除了根节点的val后的值
            FindPath(root.left, target); 
            FindPath(root.right, target); 
          // 回退一个node，这里强行记忆吧
            list.remove(list.size() - 1); 
            return listAll; 
        }
    }
    ```

25. ​输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

    ```java
    // 将二叉搜索树转化为排序的双向链表，其实就是讲二叉树进行中序遍历，在二叉搜索树中这样能够保证得到一个排序后的结果，进而，将指针进行变换即可
    public class Solution {
        public TreeNode Convert(TreeNode pRootOfTree) {
            if (pRootOfTree == null) {
                return null;
            }
            
            if (pRootOfTree.left == null && pRootOfTree.right == null) {
                return pRootOfTree;
            }
            
            // 得到左边已编程双向链表的结果
            TreeNode left = Convert(pRootOfTree.left);
            TreeNode p = left;
            // 得到左子树最右节点
            while (p != null && p.right != null) {
                p = p.right;
            }
            // 如果左子树不为空，将root添加到左子树末尾
            if (left != null) {
                p.right = pRootOfTree;
                pRootOfTree.left = p;
            }
            // 处理右子树
            TreeNode right = Convert(pRootOfTree.right);
            if (right != null) {
                pRootOfTree.right = right;
                right.left = pRootOfTree;
            }
            
            return left != null ? left : pRootOfTree;
        }
    }
    ```

26. 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

    ```java
    public class Solution {
        public int MoreThanHalfNum_Solution(int [] array) {
            if (array == null || array.length == 0) {
                return 0;
            }
            
            int times = 1;
            int result = array[0];
            for (int i = 1; i < array.length; i++) {
                if (times == 0) {
                    result = array[i];
                    times = 1;
                }else if (array[i] == result) {
                    times++;
                } else {
                    times--;
                }
            }
            
            if (CheckMoreThanHalf(array, result)){
                return result;
            } else {
                return 0;
            }
        }
        
        public boolean CheckMoreThanHalf (int[] array, int number) {
            int times = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] == number) {
                    times++;
                }
            }
            if (times * 2 <= array.length) {
                return false;
            }
            return true;
        }
    }
    ```

27. ​