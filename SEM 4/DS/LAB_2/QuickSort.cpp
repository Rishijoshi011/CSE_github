#include <iostream>

using namespace std;

inline void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partitioning(int* arr, int lowerIndex, int higherIndex) {
    int pivot = arr[higherIndex];
    int i = (lowerIndex - 1);

    for (int j = lowerIndex; j <= higherIndex - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[higherIndex]);
    return (i + 1);
}   

void quickSort(int* arr, int lowerIndex, int higherIndex) {
    if (lowerIndex < higherIndex) {
        int n = partitioning(arr, lowerIndex, higherIndex);
        quickSort(arr, lowerIndex, n - 1);
        quickSort(arr, n + 1, higherIndex);
    }
}

int main() {
    cout << "Enter size of an Array" << endl;
    int size;
    cin >> size;

    int arr[size];

    cout << "Enter elements of an Array" << endl;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    quickSort(arr, 0, size - 1);

    cout << "After sort: " << endl;
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }

/*
// BB Bhai
#include <iostream>
using namespace std;

int quick(int a[], int s, int e)
{
    int p = a[s];
    int count = 0;

    for (int i = s + 1; i <= e; i++)
    {
        if (a[i] <= p)
        {
            count++;
        }
    }

    int pind = s + count;
    swap(a[pind], a[s]);

    int i = s, j = e;

    while (i < pind && j > pind)
    {
        while (a[i] <= p)
        {
            i++;
        }
        while (a[j] > p)
        {
            j--;
        }
        if (i < pind && j > pind)
        {
            swap(a[i++], a[j--]);
        }
    }
    return pind;
}

void quickSort(int a[], int s, int e)
{
    if (s >= e)
    {
        return;
    }

    int p = quick(a, s, e);

    quickSort(a, s, p - 1);

    quickSort(a, p + 1, e);
}

int main()
{
    int a[] = {9, 3, 4, 69, 1, -2};
    int n = 6;

    quickSort(a, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}

*/