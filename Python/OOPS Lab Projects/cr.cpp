#include<iostream>
#include<iomanip>
using namespace std;
class details{
        protected:
            string nameofcustomer;
            int car_brand;
            string car_Number;
};
class rent:public details{
        protected:
            int rentfee;
            int days;
        public:
            initial();
            void greeting();
            void data();
            void rentamount();
            void record();
};
rent::initial(){
	rentfee=0;
	days=0;
}
void rent::greeting(){
    cout<<"\t\t\t~~~~~~~~~~~~~~Welcome To My Car Rental System Project~~~~~~~~~~~~~~~\n";
    cout<<"\n\t\t\t\t\t     >>>>>>>>>>>>>MADE BY<<<<<<<<<<<<"<<endl;
    cout<<"\n\n\t\t\t\t\t--------||Name: "<<"\tPRAGYA SHARMA"<<"-------||"<<endl;
    cout<<"\t\t\t\t\t--------||Roll No: "<<"\tUE228079"<<"------||"<<endl;
	cout<<"\n\n\t\t\t\t\t\t_____________________"<<endl;
	cout<<"\t\t\t\t\t\t|                   |"<<endl;
	cout<<"\t\t\t\t\t\t|                   |"<<endl;
	cout<<"\t\t\t\t\t\t|                   |__________"<<endl;
	cout<<"\t\t\t\t\t\t|                              |]"<<endl;
	cout<<"\t\t\t\t\t\t|__-----____________----_______|]"<<endl;
	cout<<"\t\t\t\t\t\t   (   )            (   )"<<endl;
	cout<<"\t\t\t\t\t\t________________________________"<<endl;
}

void rent::data(){
	cout << "\n\n\t\t\tEnter Customer's Name here: ";
  	cin >> nameofcustomer;

    do{
	    cout << "\t\t\t\t**********Select a car:-************\n ";
		cout << "\t\t\t\t 1.2023 Hyundai Creta"<<endl;
	    cout << "\t\t\t\t 2.2023 Toyota Urban Cruiser"<<endl;
	    cout << "\t\t\t\t 3.2023 Maruti Suzuki Ertiga"<<endl;
	    cout << endl;
	    cout << "\t\t\t\tPlease Select: ";
	    cin >> car_brand;
	    cout << endl;
	 			
	 	switch(car_brand){
	 		case 1:
	 			cout<<"\t\t\tYou have selected 2023 Hyundai Creta"<<endl;
				break;
			case 2:
	  			cout<<"\t\t\tYou have selected 2023 Toyota Urban Cruiser"<<endl;
				break;	
			case 3:
		     	cout<<"\t\t\tYou have selected 2023 Maruti Suzuki Ertiga"<<endl;
		   		break;  			
			default:
		     	cout<<"\t\t\tSorry!!Car of this brand is unavailable."<<endl;
		}
//        if(car_brand==1){
//        		cout<<"You have selected 2023 Hyundai Creta"<<endl;
//		}
//		else if(car_brand==2){
//			cout<<"You have selected 2023 Toyota Urban Cruiser"<<endl;
//		}
//		else if(car_brand==3){
//				cout<<"You have selected 2023 Maruti Suzuki Ertiga"<<endl;
//		}
//		else{
//			cout<<"Sorry!!Car of this brand is unavailable."<<endl;
//		}
	}while(car_brand>3);

	    	
	
	
}
void rent::rentamount(){
    cout<<"\n\n\t\tEnter number of days for which you want the car for rent: ";
	cin >> days;
	cout<<endl;
	if(car_brand == 1)
		rentfee = days*300;
	if(car_brand == 2)
		rentfee = days*350;
	if(car_brand == 3)
		rentfee = days*250;
}
void rent::record(){
	cout<<"\n"<<endl;
	cout<<"\t\t                       ________________               "<<endl;
	cout<<"\t\t                      |                |"<<endl;
	cout<<"\t\t                      |CUSTOMER DETAILS|                "<<endl;
	cout<<"\t\t                      |________________|"<<endl;
	
	
	cout << "\n\n\t\t	  Customer Name "<<"\t\t"<< nameofcustomer<<endl;
	cout << "\t\t	  Car Brand  "<<"\t\t\t"<<car_brand<<endl;     
	cout << "\t\t	  Number of days(rented) "<<"\t"<<days<<endl;
	cout << "\t\t	  Rental Amount  "<<"\t\t"<<rentfee<<endl;
	
	cout << "\n\t\t	  [Total Rental Amount  "<<"= "<<"Rs"<<rentfee<<"]"<<endl;
	cout << "\n\n\t\t	****NOTE:\n\t\t\tYou are advised to pay up the amount before due date."<<endl;
	cout << "\t\t	Otherwise penelty fee will be applied****"<<endl;
	cout<<"\n\n\t\t\t\t\t~~~~~~~~~~~~HAPPY JOURNEY!~~~~~~~~~~~~";
	
	
}
	
 int main(){
	rent r; 
	r.greeting();
	r.data();
    r.rentamount();
    r.record();
	return 0;
}
	

            
