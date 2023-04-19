# ArithmetricFormatter
Create a function that receives a list of strings that are arithmetic problems and 
returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. 
When the second argument is set to True, the answers should be displayed.

Input:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
