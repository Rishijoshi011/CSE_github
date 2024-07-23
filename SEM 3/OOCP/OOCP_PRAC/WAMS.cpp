#include <iostream>
#include <string>
#include <stdexcept>
#include <fstream>
#include <iomanip>

using namespace std;

class Customer
{
    int id, age, pwChoice;
    string customerName;

public:
    void set(string customerName, int age)
    {
        this->customerName = customerName;
        this->age = age;
    }

    void get()
    {
        cout << "Customer Name: " << customerName << endl;
        cout << "Customer Name: " << age << endl;
    }
    friend class FinalPrinting;
};

class FireArms
{
    int id;
    int price;
    string name;

public:
};

class AssultRifles
{
    const static int classId;
    int ar;
    const string weapons[10];
    string finalAR;
    int finalPrice;
    const int price[10];

public:
    AssultRifles() : ar(0), weapons{"M4 Carbine", "M16", "AK-47", "AUG A3", "FAMAS F1", "FN SCAR - L", "Travor X95", "Heckler & Koch HK416", "QBZ-95", "CZ 805 BREN"}, price{1000, 1200, 1500, 1400, 1600, 1800, 2000, 2100, 1900, 1700} {}

    string getFinalAR() { return finalAR; }

    int getFinalARPrice() { return finalPrice; }

    void setPrimaryArm()
    {
        cout << "Here's The available Stock: " << endl
             << endl;
        for (int i = 0; i < 10; i++)
        {
            cout << i + 1 << "." << weapons[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> ar;

            if (ar < 1 || ar > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (ar < 1 || ar > 10);
        finalAR = weapons[ar - 1];
        finalPrice = price[ar - 1];
    }

    void getPrimaryArm()
    {
        cout << "Slected Fire-Arm is: " << weapons[ar - 1] << endl;
        cout << "Price: " << price[ar - 1] << endl;
    }
};

class SubMachines
{
    const static int classId;
    int smg;
    const string weapons[10];
    string finalSMG;
    int finalPrice;
    const int price[10];

public:
    SubMachines() : smg(0), weapons{"MP5", "Uzi", "PP-19 Bizon", "MAC-10", "Thompson", "Vector", "Scorpion EVO", "MP7", "P90", "Kriss Vector"}, price{600, 500, 700, 450, 550, 650, 750, 700, 650, 700} {}

    string getFinalSMG() { return finalSMG; }
    int getFinalSMGPrice() { return finalPrice; }

    void setPrimaryArm()
    {
        cout << "Here's The available Stock: " << endl
             << endl;
        for (int i = 0; i < 10; i++)
        {
            cout << i + 1 << "." << weapons[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> smg;

            if (smg < 1 || smg > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (smg < 1 || smg > 10);
        finalSMG = weapons[smg - 1];
        finalPrice = price[smg - 1];
    }

    void getPrimaryArm()
    {
        cout << "Selected Fire-Arm is: " << weapons[smg - 1] << endl;
        cout << "Price: " << price[smg - 1];
    }
};

class Shotguns
{
    const static int classId;
    int shotgun;
    const string weapons[10];
    string finalShot;
    int finalPrice;
    int price[10];

public:
    Shotguns() : shotgun(0), weapons{"Remington 870", "Mossberg 500", "Benelli M4", "Winchester Model 1897", "Ithaca 37", "Saiga-12", "Franchi SPAS-12", "Stoeger Double Defense", "Browning BPS", "Winchester SXP"}, price{800, 750, 900, 850, 750, 950, 1000, 900, 800, 850} {}

    int getFinalShotgunPrice() { return finalPrice; }
    string getFinalShotgun() { return finalShot; }

    void setPrimaryArm()
    {
        cout << "Here's The available Stock: " << endl
             << endl;
        for (int i = 0; i < 10; i++)
        {
            cout << i + 1 << "." << weapons[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> shotgun;

            if (shotgun < 1 || shotgun > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (shotgun < 1 || shotgun > 10);
        finalShot = weapons[shotgun - 1];
        finalPrice = price[shotgun - 1];
    }

    void getPrimaryArm()
    {
        cout << "Selected Fire-Arm is: " << weapons[shotgun - 1] << endl;
        cout << "Price is: " << price[shotgun - 1] << endl;
    }
};

class PrimaryWeapon : public FireArms
{
    int id, chosenCatagory;
    string finalName, typeOfPrim[3];
    int finalPrice;
    AssultRifles ar;
    SubMachines sub;
    Shotguns shot;

public:
    PrimaryWeapon() : id(0), finalName(""), typeOfPrim{"Assult Rifle", "Sub Machines", "Shotguns"}, finalPrice(0) {}
    void choosePrimaryWeapon()
    {
        cout << "Which type of weapon you should like to carry as a primary weapon" << endl
             << endl;
        for (int i = 0; i < 3; i++)
        {
            cout << i + 1 << "." << typeOfPrim[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> chosenCatagory;

            if (chosenCatagory < 1 || chosenCatagory > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (chosenCatagory < 1 || chosenCatagory > 10);

        callingCatagory();
    }

    void getPrimaryWeapon()
    {
        cout << "Slected Fire-Arm catagory is: " << typeOfPrim[chosenCatagory - 1] << endl;
    }

    void callingCatagory()
    {
        while (true)
        {
            if (chosenCatagory >= 1 && chosenCatagory <= 3)
            {
                try
                {
                    switch (chosenCatagory)
                    {
                    case 1:
                        ar.setPrimaryArm();
                        finalPrice = ar.getFinalARPrice();
                        finalName = ar.getFinalAR();
                        break;

                    case 2:
                        sub.setPrimaryArm();
                        finalPrice = sub.getFinalSMGPrice();
                        finalName = sub.getFinalSMG();
                        break;

                    case 3:
                        shot.setPrimaryArm();
                        finalPrice = shot.getFinalShotgunPrice();
                        finalName = shot.getFinalShotgun();
                        break;

                    default:
                        throw runtime_error("category exception");
                        break;
                    }
                }
                catch (const exception &e)
                {
                    std::cerr << e.what() << '\n';
                }
                break;
            }
            else
            {
                cout << "Invalid choice. Please enter 1, 2, or 3." << endl;
                cout << "Enter the category (1 for Assult Rifle, 2 for Sub Machines, 3 for Shotguns): ";
                cin >> chosenCatagory;
            }
        }
    }

    void finalSelection()
    {
        if (chosenCatagory == 1)
        {
            ar.getPrimaryArm();
        }
        else if (chosenCatagory == 2)
        {
            sub.getPrimaryArm();
        }
        else if (chosenCatagory == 3)
        {
            shot.getPrimaryArm();
        }
    }
    friend class FinalPrinting;
};

class Pistols
{
    int pistol;
    const static int classId;
    const string weapons[10];
    const int price[10];
    string finalName;
    int finalprice;

public:
    string getFinalPistol() { return finalName; }
    int getFinalPistolPrice() { return finalprice; }

    Pistols() : pistol(0), weapons{"Glock 17", "Beretta 92", "SIG Sauer P226", "Smith & Wesson M&P", "H&K USP", "CZ 75", "1911", "Walther PPK", "Ruger LCP", "Desert Eagle"}, price{500, 600, 700, 550, 800, 650, 900, 550, 450, 1000} {}

    void setSecondaryArm()
    {
        cout << "Here's The available Stock of Pistols: " << endl
             << endl;
        for (int i = 0; i < 10; i++)
        {
            cout << i + 1 << "." << weapons[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> pistol;

            if (pistol < 1 || pistol > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (pistol < 1 || pistol > 10);
        finalprice = price[pistol - 1];
        finalName = weapons[pistol - 1];
    }

    void getSecondaryArm()
    {
        cout << "Selected Pistol is: " << weapons[pistol - 1] << endl;
    }
};

class Knives
{
    int knife;
    const static int classId;
    const string weapons[10];
    const int price[10];
    int finalPrice;
    string finalName;

public:
    Knives() : knife(0), weapons{"Bowie Knife", "Karambit", "Tanto", "Butterfly Knife", "Dagger", "Machete", "Throwing Knife", "Survival Knife", "Combat Knife", "Boot Knife"}, price{100, 250, 150, 200, 90, 120, 50, 80, 70, 60} {}

    int getFinalKnivesPrice() { return finalPrice; }
    string getFinalKnives() { return finalName; }

    void setSecondaryArm()
    {
        cout << "Here's The available Stock of Knives: " << endl
             << endl;
        for (int i = 0; i < 10; i++)
        {
            cout << i + 1 << "." << weapons[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> knife;

            if (knife < 1 || knife > 10)
            {
                cout << "Invalid choice. Please choose a number from 1 to 10." << endl;
            }
        } while (knife < 1 || knife > 10);
        finalPrice = price[knife - 1];
        finalName = weapons[knife - 1];
    }

    void getSecondaryArm()
    {
        cout << "Selected Knife is: " << weapons[knife - 1] << endl;
    }
};

class SecondaryWeapon : public FireArms
{
    int id, chosenCatagory;
    string finalName, typeOfSecondary[2];
    int finalPrice;
    Pistols pistols;
    Knives knives;

public:
    SecondaryWeapon() : id(0), finalName(""), typeOfSecondary{"Pistols", "Knives"} {}

    void chooseSecondaryWeapon()
    {
        cout << "Which type of weapon you should like to carry as a Secondary weapon" << endl
             << endl;
        for (int i = 0; i < 2; i++)
        {
            cout << i + 1 << "." << typeOfSecondary[i] << endl;
        }

        do
        {
            cout << endl
                 << "Enter choice: ";
            cin >> chosenCatagory;

            if (chosenCatagory < 1 || chosenCatagory > 2)
            {
                cout << "Invalid choice. Please choose a 1 or 2." << endl;
            }
        } while (chosenCatagory < 1 || chosenCatagory > 2);

        callingCatagory();
    }

    void getSecondaryWeapon()
    {
        cout << "Slected Fire-Arm catagory is: " << typeOfSecondary[chosenCatagory - 1] << endl;
    }

    void callingCatagory()
    {
        while (true)
        {
            if (chosenCatagory >= 1 && chosenCatagory <= 3)
            {
                try
                {
                    switch (chosenCatagory)
                    {
                    case 1:
                        pistols.setSecondaryArm();
                        finalName = pistols.getFinalPistol();
                        finalPrice = pistols.getFinalPistolPrice();
                        break;

                    case 2:
                        knives.setSecondaryArm();
                        break;

                    default:
                        throw runtime_error("category exception");
                        break;
                    }
                }
                catch (const exception &e)
                {
                    std::cerr << e.what() << '\n';
                }
                break;
            }
            else
            {
                cout << "Invalid choice. Please enter 1, 2, or 3." << endl;
                cout << "Enter the category (1 for Assult Rifle, 2 for Sub Machines, 3 for Shotguns): ";
                cin >> chosenCatagory;
            }
        }
    }

    void finalSelection()
    {
        if (chosenCatagory == 1)
        {
            pistols.getSecondaryArm();
        }
        else if (chosenCatagory == 2)
        {
            knives.getSecondaryArm();
        }
    }
    friend class FinalPrinting;
};

class FinalPrinting
{
    PrimaryWeapon &pw;
    SecondaryWeapon &sw;
    Customer &cust;

public:
    FinalPrinting(Customer &cust, PrimaryWeapon &pw, SecondaryWeapon &sw) : cust(cust), pw(pw), sw(sw) {}

    void confirmOrder()
    {
        ofstream outPut("order.txt");

        outPut << setfill('-') << setw(41) << "RIAUHAS AMMUNATION";
        outPut << setfill('-') << setw(21) << "-" << endl
               << endl;

        outPut << "Customer Name: " << cust.customerName << endl;
        outPut << "Customer Age: " << cust.age << endl;

        outPut << endl
               << endl;

        outPut << setfill('*') << setw(41) << "PRIMARY WEAPON";
        outPut << setfill('*') << setw(21) << "*" << endl;

        outPut << endl
               << endl;

        outPut << "Product Name: " << pw.finalName << endl;
        outPut << "Product Price: " << pw.finalPrice << endl;
        outPut << "Product Category: " << pw.typeOfPrim[pw.chosenCatagory - 1] << endl;

        outPut << endl
               << endl;

        outPut << setfill('*') << setw(41) << "SECONDARY WEAPON";
        outPut << setfill('*') << setw(21) << "*" << endl;

        outPut << endl
               << endl;

        outPut << "Product Name: " << sw.finalName << endl;
        outPut << "Product Price: " << sw.finalPrice << endl;
        outPut << "Product Category: " << sw.typeOfSecondary[sw.chosenCatagory - 1] << endl;

        outPut << endl
               << setfill('-') << setw(62) << "-";
        outPut.close();
    }
};

const int AssultRifles::classId = 1;
const int SubMachines::classId = 2;
const int Shotguns::classId = 3;
const int Pistols::classId = 4;
const int Knives::classId = 5;

int main()
{
    Customer cust;
    PrimaryWeapon pw;
    SecondaryWeapon sw;
    FinalPrinting fp(cust, pw, sw);
    string customerName;
    int age;

    cout << "Enter Your Name: ";
    cin >> customerName;
    cout << "Enter Your Age: ";
    cin >> age;
    cust.set(customerName, age);

    if (age > 22)
    {
        pw.choosePrimaryWeapon();
        pw.finalSelection();

        sw.chooseSecondaryWeapon();
        sw.finalSelection();

        fp.confirmOrder();
    }
    else
    {
        cout << "You're not leagal age to buy Fire-Arms" << endl;
    }

    return 0;
}