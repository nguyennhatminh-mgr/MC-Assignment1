import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    #test identifier
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
        self.assertTrue(TestLexer.checkLexeme("123aAsVN","123,aAsVN,<EOF>",104))
        self.assertTrue(TestLexer.checkLexeme("true8","true8,<EOF>",105))
    def test_identifier_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc123e12.3","abc123e12,.3,<EOF>",107))
    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("12akh kli_0909-1","12,akh,kli_0909,-,1,<EOF>",108))

    #test integer
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",109))
    def test_integer_1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a+789==4","123,a,+,789,==,4,<EOF>",110))
    def test_integer_2(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123.a+69--/4","123.,a,+,69,-,-,/,4,<EOF>",111))

    #test block comments
    def test_block_comment(self):
        """test block comments"""
        self.assertTrue(TestLexer.checkLexeme("/*this is a comment \n*/","<EOF>",112))
    def test_block_comment_1(self):
        """test block comments"""
        self.assertTrue(TestLexer.checkLexeme("/*this is // white space \n*/","<EOF>",114))
    def test_block_comment_2(self):
        """test block comments"""
        self.assertTrue(TestLexer.checkLexeme("/*\\nr\t\a\b\i \\*/","<EOF>",115))
    def test_block_comment_3(self):
        """test block comments"""
        self.assertTrue(TestLexer.checkLexeme("/*123 \n @abc \r \t \n*/","<EOF>",113))
    #test line comments
    def test_line_comment(self):
        """test line comments"""
        self.assertTrue(TestLexer.checkLexeme("//this is a  line comment","<EOF>",116))
    def test_line_comment_1(self):
        """test line comments"""
        self.assertTrue(TestLexer.checkLexeme("//this is a \n line comment","line,comment,<EOF>",117))
    def test_line_comment_2(self):
        """test line comments"""
        self.assertTrue(TestLexer.checkLexeme("//PPL lover \n","<EOF>",118))
    
    #test key words
    def test_keyword(self):
        """test key words"""
        self.assertTrue(TestLexer.checkLexeme("true _abc","true,_abc,<EOF>",119))
    def test_keyword_1(self):
        """test key words"""
        self.assertTrue(TestLexer.checkLexeme("true false if else ifelse","true,false,if,else,ifelse,<EOF>",120))
    def test_keyword_2(self):
        """test key words"""
        self.assertTrue(TestLexer.checkLexeme("if(hello==false) return true;","if,(,hello,==,false,),return,true,;,<EOF>",121))
 
    #test operators
    def test_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a+b","a,+,b,<EOF>",122))
    def test_operator_1(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a+b>=c","a,+,b,>=,c,<EOF>",123))
    def test_operator_2(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("x+y>=||false+true=if","x,+,y,>=,||,false,+,true,=,if,<EOF>",124))
    def test_operator_3(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a+b>=||_c*/8%a false","a,+,b,>=,||,_c,*,/,8,%,a,false,<EOF>",204))
    def test_operator_4(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("<=<!=>=||%/*-+","<=,<,!=,>=,||,%,/,*,-,+,<EOF>",205))
    def test_operator_5(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("false>=true","false,>=,true,<EOF>",206))
    def test_operator_6(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("if!=return;","if,!=,return,;,<EOF>",207))
    def test_operator_7(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("void a/b%c","void,a,/,b,%,c,<EOF>",208))

    #test boolean literals
    def test_boolean_lit(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("boolean a; \n a = true","boolean,a,;,a,=,true,<EOF>",125))
    def test_boolean_lit_1(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("boolean a = false;","boolean,a,=,false,;,<EOF>",126))
    def test_boolean_lit_2(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("console,log(a=true)","console,,,log,(,a,=,true,),<EOF>",127))
    
    #test float literals
    def test_float_lit(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.1e12abc","1.1e12,abc,<EOF>",128))
    def test_float_lit_1(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme(".9c12 abc",".9,c12,abc,<EOF>",130))
    def test_float_lit_2(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1e34x abc","1e34,x,abc,<EOF>",132))
    def test_float_lit_3(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1E-34x2 3.90e-38 abc","1E-34,x2,3.90e-38,abc,<EOF>",133))
    def test_float_lit_4(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1E0+34*2-abc=true if break","1E0,+,34,*,2,-,abc,=,true,if,break,<EOF>",134))
    def test_float_lit_5(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.c12 abc","1.,c12,abc,<EOF>",129))
    def test_float_lit_6(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme(".9E-12 abc",".9E-12,abc,<EOF>",131))
    def test_float_lit_7(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("-.9e-16 abc","-,.9e-16,abc,<EOF>",195))
    def test_float_lit_8(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("1E0-12 abc","1E0,-,12,abc,<EOF>",196))
    def test_float_lit_9(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("-9.e-12+10 abc","-,9.e-12,+,10,abc,<EOF>",197))
    def test_float_lit_10(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("3.1E12+4e0 abc","3.1E12,+,4e0,abc,<EOF>",198))
    def test_float_lit_11(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("-.10E-10 xyz","-,.10E-10,xyz,<EOF>",199))

    #test string literals
    def test_string_lit(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is a string"','this is a string,<EOF>',135))
        self.assertTrue(TestLexer.checkLexeme('"this \'is\' a test\\n"','this \'is\' a test\\n,<EOF>',136))
    def test_string_lit_1(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is a string\"','this is a string,<EOF>',137))
    def test_string_lit_2(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is a string\\""','this is a string\\",<EOF>',138))
    def test_string_lit_3(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is a string \a"','this is a string \a,<EOF>',139))
    def test_string_lit_4(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is \\"a\\" string \a"','this is \\"a\\" string \a,<EOF>',140))
    def test_string_lit_5(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is \\ string"','Illegal Escape In String: this is \ ',141))
    def test_string_lit_6(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is \i string"','Illegal Escape In String: this is \i',142))
    def test_string_lit_7(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is \\\ string"','this is \\\ string,<EOF>',143))
    def test_string_lit_8(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is my string','Unclosed String: this is my string',144))
    def test_string_lit_9(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this a test \ case"','Illegal Escape In String: this a test \ ',145))
        self.assertTrue(TestLexer.checkLexeme('"this a test \n case"','Unclosed String: this a test ',146))
    def test_string_lit_10(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\n"','Unclosed String: ',147))
    def test_string_lit_11(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"Hello world ! \\n"','Hello world ! \\n,<EOF>',148))
    def test_string_lit_12(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('Now is 530PM 7/9/2019 != \n"','Now,is,530,PM,7,/,9,/,2019,!=,Unclosed String: ',149))
    def test_string_lit_13(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this is unclosed string','Unclosed String: this is unclosed string',150))
    def test_string_lit_14(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"test tab    tab"','test tab    tab,<EOF>',151))
    def test_string_lit_15(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('a+b=c"\n"','a,+,b,=,c,Unclosed String: ',152))
    def test_string_lit_16(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('x*y=z"\l"','x,*,y,=,z,Illegal Escape In String: \l',153))
    def test_string_lit_17(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\\n \\t \\b \\i \k"','Illegal Escape In String: \\n \\t \\b \\i',154))
    def test_string_lit_18(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\\n \\t \\b" "\\i \k"','\\n \\t \\b,Illegal Escape In String: \i',155))
    def test_string_lit_19(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\\b"','\\b,<EOF>',156))
    def test_string_lit_20(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\b','Unclosed String: ',160))
    def test_string_lit_21(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\f','Unclosed String: ',161))
    def test_string_lit_22(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"\f"','Unclosed String: ',162))
    def test_string_lit_23(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this"','this,<EOF>',163))
    def test_string_lit_24(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"How to pass PPL?"','How to pass PPL?,<EOF>',200))
    def test_string_lit_25(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"this \\""','this \\",<EOF>',209))
    def test_string_lit_26(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"a+b=c"','a+b=c,<EOF>',210))
    

    #test error token
    def test_error_token(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('xyz$#@abc','xyz,Error Token $',157))
    def test_error_token_1(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('%+-@ghj','%,+,-,Error Token @',158))
    def test_error_token_2(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('a%b+c-d=f;@ghj','a,%,b,+,c,-,d,=,f,;,Error Token @',159))
    def test_error_token_3(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('c-d=f;#ghj','c,-,d,=,f,;,Error Token #',191))
    def test_error_token_4(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('"@$%#!"','@$%#!,<EOF>',192))
    def test_error_token_5(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('x+y=z;^ghj','x,+,y,=,z,;,Error Token ^',193))
    def test_error_token_6(self):
        """test errors token"""
        self.assertTrue(TestLexer.checkLexeme('(-.-)','(,-,Error Token .',194))

    #test array
    def test_array(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('int a[10]={1,2,3}','int,a,[,10,],=,{,1,,,2,,,3,},<EOF>',164))
    def test_array_1(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('int a[10]; float b[27];','int,a,[,10,],;,float,b,[,27,],;,<EOF>',165))
    def test_array_2(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('int a[20]; a[2]=9;','int,a,[,20,],;,a,[,2,],=,9,;,<EOF>',166))
    def test_array_3(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('int a[10]; int b[10]; int c[10]; c[3]=a[5]+b[9];'
                                            ,'int,a,[,10,],;,int,b,[,10,],;,int,c,[,10,],;,c,[,3,],=,a,[,5,],+,b,[,9,],;,<EOF>',181))
    def test_array_4(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('string arr[10]; putStringLn(arr);','string,arr,[,10,],;,putStringLn,(,arr,),;,<EOF>',182))
    def test_array_5(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme('float arr[10]; putStringLn(arr[5]);','float,arr,[,10,],;,putStringLn,(,arr,[,5,],),;,<EOF>',183))
       
    #test for loop
    def test_for_loop(self):
        """test for loop"""
        self.assertTrue(TestLexer.checkLexeme('for(int i=0;i<10;i++){}','for,(,int,i,=,0,;,i,<,10,;,i,+,+,),{,},<EOF>',167))
    def test_for_loop_1(self):
        """test for loop"""
        self.assertTrue(TestLexer.checkLexeme('for(;true;){k=k+1;}','for,(,;,true,;,),{,k,=,k,+,1,;,},<EOF>',168))
    def test_for_loop_2(self):
        """test for loop"""
        self.assertTrue(TestLexer.checkLexeme('int i=0; for(;true;){if(i==10) break; i++;}',
                                            'int,i,=,0,;,for,(,;,true,;,),{,if,(,i,==,10,),break,;,i,+,+,;,},<EOF>',169))
    def test_for_loop_3(self):
        """test for loop"""
        self.assertTrue(TestLexer.checkLexeme('int arr[10];for(int i=0;i<10;i++){arr[i]=i*i;}',
                            'int,arr,[,10,],;,for,(,int,i,=,0,;,i,<,10,;,i,+,+,),{,arr,[,i,],=,i,*,i,;,},<EOF>',170))

    #test while loop
    def test_while_loop(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme('while(true){}','while,(,true,),{,},<EOF>',171))
    def test_while_loop_1(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme('while(true){ if(k) break;}','while,(,true,),{,if,(,k,),break,;,},<EOF>',172))
    def test_while_loop_2(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme('int i=10;while(i>=10){ k++;}','int,i,=,10,;,while,(,i,>=,10,),{,k,+,+,;,},<EOF>',173))
    def test_while_loop_3(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme('int i=10;while(i>=10){ arr[i]="true";}','int,i,=,10,;,while,(,i,>=,10,),{,arr,[,i,],=,true,;,},<EOF>',174))

    #test function
    def test_function(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('int f(){return var;}','int,f,(,),{,return,var,;,},<EOF>',175))
    def test_function_1(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('float func(){return var;}','float,func,(,),{,return,var,;,},<EOF>',176))
    def test_function_2(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('string func(){return var;}','string,func,(,),{,return,var,;,},<EOF>',177))
    def test_function_3(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('boolean func(){return true;}','boolean,func,(,),{,return,true,;,},<EOF>',178))
    def test_function_4(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('int main(){ putString("Hello world!\\n");}',
                'int,main,(,),{,putString,(,Hello world!\\n,),;,},<EOF>',179))
    def test_function_5(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme('int main(){ putStringLn("Hello world!");}',
                'int,main,(,),{,putStringLn,(,Hello world!,),;,},<EOF>',180))
    
    #test pointer
    def test_pointer(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('int *a;','int,*,a,;,<EOF>',184))
    def test_pointer_1(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('int **a;','int,*,*,a,;,<EOF>',185))
    def test_pointer_2(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('float *a; a=new float()[];','float,*,a,;,a,=,new,float,(,),[,],;,<EOF>',186))
    def test_pointer_3(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('string *a="Minh";','string,*,a,=,Minh,;,<EOF>',187))
    def test_pointer_4(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('int *a; int arr[10]; a=arr;','int,*,a,;,int,arr,[,10,],;,a,=,arr,;,<EOF>',188))
    def test_pointer_5(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('boolean *a,*b,*c;','boolean,*,a,,,*,b,,,*,c,;,<EOF>',189))
    def test_pointer_6(self):
        """test pointer"""
        self.assertTrue(TestLexer.checkLexeme('void *x,*y,*z;','void,*,x,,,*,y,,,*,z,;,<EOF>',190))
    # def test_pointer_7(self):
    #     """test pointer"""
    #     self.assertTrue(TestLexer.checkLexeme('"abc"adc"','abc,adc,Unclosed String: ',370))
    # def test_pointer_8(self):
    #     """test pointer"""
    #     self.assertTrue(TestLexer.checkLexeme('"abc \b abc"','Unclosed String: abc ',371))
    # #test for some string
    # def test_string(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",372))
    # def test_unclose_string(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,373))
    # def test_illegal_escape(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",374))
    # def test_double_slash(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",375))
    # def test_double_slash_1(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",376))
    # def test_double_slash_2(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "\\"123 \\"" ""","""\,123,,<EOF>""",377))
    