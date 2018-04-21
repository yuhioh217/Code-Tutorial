#include <stdio.h>

int main(void)
{
   int i = 20;    //declare the integer type parameter.
   char _c = 'A'; //notice that the naming rule can use the "_" in the star of the string.
   char *s = "apple"; //declare the char*(string) type s   

   printf("Integer \"i\" is %d\n", i);
   printf("Character \"_c\" is %c\n" , _c);
   printf("String \"s\" is %s\n", s);

   return 0;
}
