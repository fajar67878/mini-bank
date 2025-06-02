#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 100; i++)
    {        
        if (i % 2 == 0)
        {
            cout << i << " YES !!! " << "\n";
        } else {
            cout << i << " NO !!! " << "\n";
        }
    }

    return 0;
}