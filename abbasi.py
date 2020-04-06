
#include<iostream>
using namespace std ;
int main()
{   string username = "hamid_ali_abbasi";
    string password = "hamid@123";
	cout<<"#########################"<<endl;
	cout<<"HAMID ALI ABBASI"<<endl;
	cout<<"03335712024"<<endl;
	cout<<"########################"<<endl;
	
    cout<<"ENTER USERNAME"<<endl;
    cin>>username;
    cout<<"ENTER PASSWORD"<<endl;
    cin>>password;
    
    if((username == "hamid_ali_abbasi") && (password ==" hamid@123"))
    {
    	cout<<"login successfull"<<endl;
	}
	else 
	{ 
	cout<<"WRONG USERNAME OR PASSWORD"<<endl;
	cout<<"ENTER USERNAME"<<endl;
    cin>>username;
    cout<<"ENTER PASSWORD"<<endl;
    cin>>password;
	}
   
    return 0;
    
}
