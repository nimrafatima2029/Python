#include <iostream>
#include <ctime>
using namespace std;


int main(){
    int N;
    int randomNumber = (rand() % 100) + 1;

    cout<<"************Guss The Number ******************"<<endl;
    cout<<"Enter the number"<<endl;
    cin>>N;

    if (N > randomNumber)
    {
        cout<<"To big number";
    }else{
        cout<<"To small number";
    }
    

}