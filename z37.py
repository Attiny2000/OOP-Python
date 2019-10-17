#include <iostream>
#include <windows.h>
#include <cstdlib>
using namespace std;

struct model_computer{
int kod_computer;
string marka_computer;
string type_processor;
int frequency_operation;
int RAM;
int HDD;
string date_prom;
float vartist_v_rublyah;
int kilkist_ekz_v_nal;
};


void add(model_computer *comp, int n)
{ SetConsoleOutputCP(1251);
 SetConsoleCP(1251);
cout<<"==========================================================================="<<endl;
for(int i=0; i<n; i++)
{
cout<<"Введіть код комп'ютера"<<endl;
cin>>comp[i].kod_computer;
cout<<"Введіть марку комп'ютера"<<endl;
cin>>comp[i].marka_computer;
cout<<"Введіть тип процесора"<<endl;
cin>>comp[i].type_processor;
cout<<"Введіть частоту роботи процесора"<<endl;
cin>>comp[i].frequency_operation;
cout<<"Введіть об'єм оперативної пам'яті"<<endl;
cin>>comp[i].RAM;
cout<<"Введіть об'єм жорсткого диску"<<endl;
cin>>comp[i].HDD;
cout<<"Введіть дату випуску на ринок"<<endl;
cin>>comp[i].date_prom;
cout<<"Введіть вартість комп'ютера в рублях"<<endl;
cin>>comp[i].vartist_v_rublyah;
cout<<"Введіть кількість екземплярів, які є в наявності"<<endl;
cin>>comp[i].kilkist_ekz_v_nal;
cout<<"==========================================================================="<<endl;
}
}
void show(model_computer *comp, int n)
{
for(int i(0); i<n; i++)
{

cout<<i+1<<") Опис ПК:"<<endl;
cout<<" Код комп'ютера :"
<<comp[i].kod_computer<<endl;
cout<<" Марка комп'ютера :"
<<comp[i].marka_computer<<endl;
cout<<" Тип процесор :"
<<comp[i].type_processor<<endl;
cout<<"Частота роботи процесора :"
<< comp[i].frequency_operation<<endl;
cout<<"Об'єм оперативної пам'яті :"
<<comp[i].RAM<<endl;
cout<<"Об'єм жоmodel_computer *comp, int nрсткого диску :"
<<comp[i].HDD<<endl;
cout<<"Дата випуску на ринок :"
<<comp[i].date_prom<<endl;
cout<<"Вартість комп'ютера в рублях :"
<<comp[i].vartist_v_rublyah<<endl;
cout<<"Кількість екземплярів, які є в наявності :"
<<comp[i].kilkist_ekz_v_nal<<endl;
cout<<"=================================================================="<<endl;
}
}

void Search_type (model_computer mass[], string type_processor, int n)
{;
for (int i = 0; i < n; i++)
{
if (type_processor == mass[i].type_processor) {
cout << " Тип комп'ютера " << mass[i].marka_computer << endl << endl;
}
else
cout << "Помилка ";
}
}

void Search_ozy (model_computer mass[], int RAM, int n)
{;
for (int i = 0; i < n; i++)
{
if (RAM == mass[i].RAM) {
cout << " Тип комп'ютера " << mass[i].marka_computer << endl << endl;
}
else
cout << "Помилка ";
}
}

void Search_data (model_computer mass[], string date_prom, int n)
{;
for (int i = 0; i < n; i++)
{
if (date_prom == mass[i].date_prom) {
cout << " Тип комп'ютера " << mass[i].marka_computer << endl << endl;
}
else
cout << "Помилка ";
}
}
int main()
{ SetConsoleOutputCP(1251);
 SetConsoleCP(1251);
string type_processor;
string date_prom;
int RAM;
cout<<"Введіть кількість даних для заповнення: ";
int n;
cin>>n;
model_computer *comp= new model_computer[n];
int key;
while(1)
{
m2:
cout<<"\t\t\t\t Меню"<<endl;
cout<<"===========================================================================\n\n";
cout<<"1) Ввід данних."<<endl;
cout<<"2) Вивести дані. "<<endl;
cout<<"3) Знайти ПК по типу процесора. "<<endl;
cout<<"4) Знайти ПК по об'єму ОЗУ. "<<endl;
cout<<"5) Знайти ПК по даті в випуску. "<<endl;
cout<<"6) Вихід."<<endl;
cout<<"7) Очистить консоль."<<endl;
cout<<"\n===========================================================================\n\n";
cout<<"Введите номер меню: "<<endl;
cin>>key;
switch(key)
{
case 1: add(comp, n); break;
case 2: show(comp, n); break;
case 3: system("cls");
cout << " Тип процесора "; cin >> type_processor;
Search_type(comp, type_processor, n); break;
case 4: system("cls");
cout << " Об'єм ОЗУ "; cin >> RAM;
Search_ozy(comp, RAM, n); break;
case 5: system("cls");
cout << " Дата випуску "; cin >> date_prom;
Search_data(comp, date_prom, n); break;
case 6: exit(1); break;
case 7: system("cls"); break;
default: cout<<"Такого пункта немає. Введіть ще раз."<<endl; goto m2;
}
}
return 0;
}
