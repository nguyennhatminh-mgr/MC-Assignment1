import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    
    #test variable declaration
    def test_var_declaration(self):
        """var declaration: int a,b,c; """
        input = """int a,b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_var_declaration_1(self):
        """var declaration:"""
        input = """int a,b,c[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_var_declaration_2(self):
        """var declaration: """
        input = """int a[0];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_var_declaration_3(self):
        """var declaration: """
        input = """int a[0],b,c[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_var_declaration_3(self):
        """var declaration: """
        input = """int a,b,c;
                float b[10];
                boolean xyz;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_var_declaration_4(self):
        """var declaration: """
        input = """int a,b,c;
                float b[];
                boolean xyz;"""
        expect = "Error on line 2 col 24: ]"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_var_declaration_5(self):
        """var declaration: """
        input = """
                int a,b,c,float b;
                float b[10];
                boolean xyz;"""
        expect = "Error on line 2 col 26: float"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_var_declaration_6(self):
        """var declaration: """
        input = """
                int a,b,c;
                float b[10], string c[0];
                boolean xyz;"""
        expect = "Error on line 3 col 29: string"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_var_declaration_7(self):
        """var declaration: """
        input = """
                int a,b,c=10;
                float b[10]; string c[0];
                boolean xyz;"""
        expect = "Error on line 2 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_var_declaration_8(self):
        """var declaration: """
        input = """
                int a,b,c;
                float b[4]={1,2,3,4}; string c[0];
                boolean xyz;"""
        expect = "Error on line 3 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    #test function declaration
    def test_func_declaration(self):
        """function declaration: """
        input = """int abc(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_func_declaration_1(self):
        """function declaration: """
        input = """int[] a(int a, int b){
            int a,b[10];
            float x,y,z;
            string str;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_func_declaration_2(self):
        """function declaration: """
        input = """int[] a(int a, int b){
            int a,b[10];
            float x,y,z;
            string str;
        }
        void a(int a[],float b,boolean c){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_func_declaration_3(self):
        """function declaration: """
        input = """float foo(string a, int b){
            int a,b[10];
            string str[4];
        }
        void a(){
            boolean b[9];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_func_declaration_4(self):
        """function declaration: """
        input = """
            float[10] foo(string a, int b){
            int a,b[10];
            string str[4];
        }
        """
        expect = "Error on line 2 col 18: 10"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_func_declaration_5(self):
        """function declaration: """
        input = """
            float] foo(string a[], int b){
            int a,b[10];
            boolean array[4];
        }
        """
        expect = "Error on line 2 col 17: ]"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_func_declaration_6(self):
        """function declaration: """
        input = """
            float[] main(string a[100], int b){
            int a,b[10];
            boolean array[4];
        }
        """
        expect = "Error on line 2 col 34: 100"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_func_declaration_7(self):
        """function declaration: """
        input = """
            float[] main(string a[], b){
            int a,b[10];
            boolean array[400+m];
        }
        """
        expect = "Error on line 2 col 37: b"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    #test expression
    def test_expression(self):
        """function expression: """
        input = """float foo(string a, int b){
            int a,b[10];
            string str[4];
        }
        int a(){
            a(a+b>c,a[a+b]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_expression_1(self):
        """function expression: """
        input = """
        int test(){
            if(a>4) return;
            i+2;
            i=i+4;
            z>=5+2;
            if(b) return z+2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_expression_2(self):
        """function expression: """
        input = """
        int test(){
            int a;
            a=a+4*6+3>5;
            a/2=p;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_expression_3(self):
        """function expression: """
        input = """
        void main(){
            if( a==b && a!=c){
                a=b;
                a=c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_expression_4(self):
        """function expression: """
        input = """
        void main(){
            if( a==b + a!=c){
                a=b;
                a=c;
            }
        }
        """
        expect = "Error on line 3 col 24: !="
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_expression_5(self):
        """function expression: """
        input = """
        void main(){
            if( a==b + (a!=c)){
                a=b;
                a=c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_expression_6(self):
        """function expression: """
        input = """
        void main(){
            if( a>=b + a<c){
                a=b;
                a=c;
            }
        }
        """
        expect = "Error on line 3 col 24: <"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_expression_7(self):
        """function expression: """
        input = """
        void main(){
            if( (a>=b) + a<c){
                a=b;
                a=c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_expression_8(self):
        """function expression: """
        input = """
        void main(){
            foo(2)[3+x]=a[b[2]]+3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_expression_9(self):
        """function expression: """
        input = """
        void main(){
            foo(2)[3+x=a[b[2]]+3;
        }
        """
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_expression_10(self):
        """function expression: """
        input = """
        void main(int a[10]){
            foo(2)[3+x]=a[b[2]]+3;
        }
        """
        expect = "Error on line 2 col 24: 10"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_expression_11(self):
        """function expression: """
        input = """
        void main(int a[],float b,string c){
            array[a[a[c]+b]]=c*b-d/a;
            x<=y || a == b ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_expression_12(self):
        """function expression: """
        input = """
        void main(int a[],float b,string c){
            array[a[a[c]+b]]=c**b-d/a;
            x<=y || a == b && c>d;
        }
        """
        expect = "Error on line 3 col 31: *"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    
    #test if statement
    def test_if_statement(self):
        """if statement """
        input = """
        int main(){
            a[4];
            if(true) return false;
            if(0.5) return z;
            if(1e2) break;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_if_statement_1(self):
        """if statement """
        input = """
        int main(){
            a[4];
            if(true && a > 5) a[foo()]=0;
            if(0.5+a==9) return z;
            if(1e2<=a) break;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_if_statement_2(self):
        """if statement """
        input = """
        {
        }
        int main(){
        }
        """
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_if_statement_3(self):
        """if statement """
        input = """
        int main(){
            if(a>b){ a =a + 1;
            break;
            continue;
            }
            else{
                a=-b;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_if_statement_4(self):
        """if statement """
        input = """
        int main(){
            if(a>b){ a =a + 1;
                break;
                continue;
            }
            else{
                if(a-b>=6) return;
                break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_if_statement_5(self):
        """if statement """
        input = """
        int main(){
            int a[10];
            if(a>b) a=a+1 else if(a<=c) return; else a>b;
        }
        """
        expect = "Error on line 4 col 26: else"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_if_statement_6(self):
        """if statement """
        input = """
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=a+1; else if(a<=c) return; else a<=b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_if_statement_7(self):
        """if statement """
        input = """
        float a(){}
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=true; else if(a<=c>d) return "o"; else a<=(b+5);
        }
        """
        expect = "Error on line 6 col 40: >"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_if_statement_8(self):
        """else lack if """
        input = """
        float a(){}
        int main(){
            else {
                a=a[a>b-c];
            }
        }
        """
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_if_statement_9(self):
        """if abundant else"""
        input = """
        int main(){
            if(c>d/a) return;
            else {
                a=a[a>b-c];
            }
            else
                a[c]==d;
        }
        """
        expect = "Error on line 7 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    #test for statement
    def test_for_statement(self):
        """for statement """
        input = """
        float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                a[i]="PPL Lover";
            }
            print("successful");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_for_statement_1(self):
        """for statement """
        input = """
        float a(){
            int a[9],i;
            for(int i=0;i<9;i=i+1){
                a[i]="PPL Lover";
            }
            print("unsuccessful");
        }
        """
        expect = "Error on line 4 col 16: int"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_for_statement_2(self):
        """for statement """
        input = """
        float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                if(i+1==9){
                    a[i]=a[0];
                    break;
                }
                a[i]=a[i+1];
            }
            print("successful");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_for_statement_3(self):
        """for statement """
        input = """
        float a(){
            int a[9],i;
            for(i=8;i>=0;i=i+2){
                if(i==false)
                    return true;
            }
            print("successful");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_for_statement_4(self):
        """for statement """
        input = """
        float a(){
            int a[9],i;
            for(i=8;;i=i+2){
                if(i==false)
                    return true;
            }
            print("successful");
        }
        """
        expect = "Error on line 4 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_for_statement_5(self):
        """for statement """
        input = """
        float main(){
            int a[10],i;
            for(){
                if(i==false)
                    return true;
            }
        }
        """
        expect = "Error on line 4 col 16: )"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    #test some special case
    def test_invalid_var_decl_case1(self):
        input = """int a,b[]; """
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_invalid_var_decl_case2(self):
        input = """int main(){
            if(5>=(a<8)){a=a+1;}
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_valid_program_5(self):
        input = """
        int main(){
            cout((array[i])[j]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    
    #test do while statement
    def test_dowhile_statement(self):
        """do while statement """
        input = """
        float a(){
            do a+b=1; while a>b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_dowhile_statement_1(self):
        """do while statement """
        input = """
        void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }while a<b+c;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_dowhile_statement_2(self):
        """do while statement """
        input = """
        void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }
            {
                int x,y,z;
                x=y+z;
            }while [a<b+c];
        }
        """
        expect = "Error on line 11 col 19: ["
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_dowhile_statement_3(self):
        """do while statement """
        input = """
        void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
                {
                    int x,y,z;
                    x=y+z;
                }
            }
            while a[a<b+c];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_dowhile_statement_4(self):
        """do while statement """
        input = """
        void main(string args[]){
            do{ 
                void var;
            }
            while a[a<b+c];
        }
        """
        expect = "Error on line 4 col 16: void"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_dowhile_statement_5(self):
        """do while statement """
        input = """
        void main(string args[]){
            do{ 
                //void var;
                -a+c=d;
            }
            while a>2.4e3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_dowhile_statement_6(self):
        """do miss while statement """
        input = """
        void main(string args[]){
            do{ 
                //void var;
                -a+c=d;
            }
            ;
        }
        """
        expect = "Error on line 7 col 12: ;"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_dowhile_statement_7(self):
        """while miss do in do while statement """
        input = """
        void main(string args[]){
            { 
                //void var;
                -a+c=d;
            }
            while (PPL==pass);
        }
        """
        expect = "Error on line 7 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_dowhile_statement_8(self):
        """do while miss ; in do while statement """
        input = """
        void main(string args[]){
            do{ 
                //void var;
                -a+c=d;
            }
            while (PPL==pass)
        }
        """
        expect = "Error on line 8 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_dowhile_statement_9(self):
        """ do while statement """
        input = """
        void main(string args[]){
            do{ 
                consolelog("string\\n");
                print(a,b,c);
                if(PPL==pass)
                    print("An mung");
            }
            while (PPL==pass);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
    def test_dowhile_statement_10(self):
        """ reverse do while role in do while statement """
        input = """
        void main(string args[]){
            while{ 
                dowhilebidao=true;
                return false;
                toPassPPL=true;
            }
            do (PPL==pass);
        }
        """
        expect = "Error on line 3 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,301))
    
    #test break statement
    def test_break_statement(self):
        """break statement """
        input = """
        float test(){
            break;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_break_statement_1(self):
        """break statement """
        input = """
        float test(){
            if(a>b)
                break;
            else
                -a/b+c*1=d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_break_statement_2(self):
        """break statement """
        input = """
        float test(){
            if(a>b)
                break a;
        }
        """
        expect = "Error on line 4 col 22: a"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_break_statement_3(self):
        """break statement """
        input = """
        float test(){
            if(true) a="I love PPL";
            if(a>b)
                break a+b>c;
        }
        """
        expect = "Error on line 5 col 22: a"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_break_statement_4(self):
        """break statement """
        input = """
        float test(){
           for(i=1;i<10;i=i+1){
               a="Principle";
               b="Programming";
               c="Language";
               z=a+b+c;
               if(z==null) break;
               print("rs = " + z);
           }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_break_statement_5(self):
        input = """float foo(){
                    string arr[]; 
                    break;              
                }
        """
        expect = "Error on line 2 col 31: ]"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    #test continue statement
    def test_continue_statement(self):
        input = """float foo(){
                    if(true) continue;           
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_continue_statement_1(self):
        input = """float foo(){
                    if(true) continue b;           
                }
        """
        expect = "Error on line 2 col 38: b"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_continue_statement_2(self):
        input = """float foo(){
                    do{
                        a=a+1;
                        if(a<0) continue;
                    }
                    while (a>10);
                    if(true) continue;           
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_continue_statement_4(self):
        input = """float foo(){
                    a=a+1;
                    if(a>10) continue;         
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_continue_statement_5(self):
        input = """
        int main(){
            cout((array[i])[j]);
            if(a>c) continue;
        }
  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_continue_statement_6(self):
        input = """
        int main(){
            do { 
                continue;
            }
            while((arr[i])[j]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    #test return statement
    def test_return_statement(self):
        input = """float foo(int a,int b){
                    return a+b;          
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_return_statement_1(self):
        input = """float gt(int n){
                    if(n==1 || n==0) return 1;
                    return n*gt(n-1);          
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_return_statement_2(self):
        input = """float gt(int n){
                    return a[a[a]];        
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_return_statement_3(self):
        input = """float gt(int n){
                    return
                }
        """
        expect = "Error on line 3 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_return_statement_4(self):
        input = """float gt(int n){
                    return a[a[a]]+b[i]==c;        
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_return_statement_5(self):
        input = """float gt(int n){
                    return a*;        
                }
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    #test expression statement
    def test_expression_statement(self):
        input = """float gt(int n){
                    n=n*n;
                    n+2;
                    100;
                    1.E2;        
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_expression_statement_1(self):
        input = """float gt(int n){
                    n=n*n;
                    gt(100,n+2);
                    1.E2;        
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_expression_statement_2(self):
        input = """float gt(int n){
                    a[a[x=y+z]]=ab;
                    x2;     
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_expression_statement_3(self):
        input = """float gt(int n){
                    a[a[x=y+z]]=ab;
                    x2     
                }
        """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    #test block statement
    def test_block_statement(self):
        input = """float gt(int n){
                    {
                        a>b;
                        a=x*y/z;
                        x2;
                        a[4];
                    }    
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_block_statement_1(self):
        input = """float gt(int n){
                        a>b;
                        a=x*y/z;
                        x2;
                        a[4];
                    }    
                }
        """
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_block_statement_2(self):
        input = """{
                    int a;
                    float b[10];                        
                }    
        """
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_block_statement_3(self):
        input = """int main(){
            float a(){}
        } 
        """
        expect = "Error on line 2 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_block_statement_4(self):
        input = """int main(){
            float a;
            a(10,a[a[7]],c+d>b);
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    def test_invalid_continue(self):
        """ID  is siminar with some keyword """
        input = """void func(){
            int continue;
            continue == continue && false;
        }
        """
        expect = "Error on line 2 col 16: continue"
    
        self.assertTrue(TestParser.checkParser(input,expect,302))
    
    def test_invalid_expression(self):
        """expression miss anry in add """
        input = """void func(){
            int a;
            +i;
        }
        """
        expect = "Error on line 3 col 12: +"
    
        self.assertTrue(TestParser.checkParser(input,expect,303))
    def test_invalid_expression_1(self):
        """expression miss anry in add """
        input = """void func(){
            int a;
            i+i;
            a-a;
            z*z+3;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_invalid_expression_2(self):
        """expression miss anry in mul """
        input = """void func(){
            int a;
            -i+a>b;
            *a=true;
        }
        """
        expect = "Error on line 4 col 12: *"
    
        self.assertTrue(TestParser.checkParser(input,expect,305))
    def test_invalid_expression_3(self):
        """expression miss anry in add """
        input = """void func(){
            int a;
            -i+a>b;
            a*a=true;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,306))
    def test_invalid_expression_4(self):
        """booleanlit in expression """
        input = """void func(){
            a=true;
            true+false=true;
            true*false=false;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,307))
    def test_invalid_expression_5(self):
        """booleanlit in expression """
        input = """void func(){
            a=true;
            array[true+false]=true*false;
            b[true[false]]=false;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,308))
    def test_invalid_expression_6(self):
        """booleanlit in expression """
        input = """void func(){
            a=true;
            array[true+false]=true*false;
            b[true[false]]=-(false+a);
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,309))
    def test_invalid_expression_7(self):
        """booleanlit in expression """
        input = """void func(){
            int a[10];
            a[0]=false;
            a[1]=-true+6/a;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,310))
    def test_invalid_expression_8(self):
        """booleanlit in expression """
        input = """void func(){
            true;
            false;
        }
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,311))
    # def test_invalid_expression_9(self):
    #     """booleanlit in expression """
    #     input = """void func(){
    #         int a;
    #         a=a+b>c;
    #         boolean b;
    #         b=false;
    #     }
    #     """
    #     expect = "successful"
    
    #     self.assertTrue(TestParser.checkParser(input,expect,312))
    # def test_invalid_expression_10(self):
    #     """booleanlit in expression """
    #     input = """void func(){
    #         int a;
    #         a=a<b==c>c;
    #         boolean b;
    #         b=false;
    #     }
    #     """
    #     expect = "successful"
    
    #     self.assertTrue(TestParser.checkParser(input,expect,313))
    
    def test_invalid_expression_20(self):
        """booleanlit in expression """
        input = """int a;
                    a=10;
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,314))
    def test_invalid_expression_21(self):
        """booleanlit in expression """
        input = """
        
        int x, y;
        int main(){
            a=123";
        }
        
        """
        expect = "successful"
    
        self.assertTrue(TestParser.checkParser(input,expect,315))