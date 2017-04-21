# PhyTestOnline
A crawler for HUST phycics test online in **python-2.7.12**. _(Not for cheating!)_

This class is specially for a HUST Physics Test Online providing a crawler to download the Keys and to save them as Excel(.xls). For convenience, you can just use `PhyTestOnline.main()` to finish the whole procedure.


## User Guide
--------------

1. Run python console (must be python2.7）, load this class, create an object of this class by typing `ans = PhyTestOnline()`.
2. Run the script by typing `ans.main()`
and it will automatically download the keys in path "**D:\TestAnswer.xls**"(The default path can be changed in function `saveAns()`).
3. The Excel file is formed by [*.jpg *] which can be seen in HTML source codes indicated the problem and the corresponding answer.

--------------

## Tips
Remember to make sure you have connected to HUST-WILELESS or likewise, which is neccessary to connect to the ip address.

---------------

## Attention
This is a simple practice in crawler, which is **only for study and communication**. It should never be used for illegal or improper ways like cheating in the exam. If so, the one who did it is responsible for his own behavior instead of the author. The author strongly suggest that every student should follow the rules and the school should fix the bugs as sooner as possible!
    
*Copyright (C) 2016 by Jerry Life. All Rights Reserved.*
