#include <iostream>
#include <vector>

using namespace std;

class Board {
public:
    std::string B[3][3] = { {".", ".", "."}, {".", ".", "."}, {".", ".", "."} };
    std::vector<int> choices;

    void draw() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << B[i][j] << " ";
            }
            cout << endl;
        }
    }

    bool strike(std::string piece) {
        int i, j, choice;
        cout << "enter(" << piece << "): ";
        cin >> choice;

        if (choice < 0 || choice > 8) {
            cout << "Invalid choice. Please try again." << endl;
            return false;
        }

        for (int x = 0; x < choices.size(); x++) {
            if (choices[x] == choice) {
                cout << "Space is taken. Please try again." << endl;
                return false;
            }
        }

        choices.push_back(choice);

        if (choice > 5) {
            i = 2;
            j = choice - 6;
        }
        else if (choice > 2 && choice <= 5) {
            i = 1;
            j = choice - 3;
        }
        else {
            i = 0;
            j = choice;
        }
        B[i][j] = piece;

        for (int k = 0; k < 3; k++) {
            if (B[k][0] == piece && B[k][1] == piece && B[k][2] == piece)
                return true;
            if (B[0][k] == piece && B[1][k] == piece && B[2][k] == piece)
                return true;
        }
        if (B[0][0] == piece && B[1][1] == piece && B[2][2] == piece)
            return true;
        if (B[0][2] == piece && B[1][1] == piece && B[2][0] == piece)
            return true;

        return false;
    }
};

int main() {
    Board b;
    int i = 0;

    while (true) {
        b.draw();
        if (i % 2 == 0) {
            if (b.strike("X")) {
                cout << endl << "X won !!" << endl;
                break;
            }
        }
        else {
            if (b.strike("O")) {
                cout << endl << "O won !!" << endl;
                break;
            }
        }
        i++;

        if (i == 9) {
            cout << endl << "It's a tie!" << endl;
            break;
        }
    }

    return 0;
}
