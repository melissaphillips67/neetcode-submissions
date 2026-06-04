class DynamicArray {
public:

    DynamicArray(int capacity) {
        arr = new int[capacity];
        cap = capacity;
    }

    int get(int i) {
        return arr[i];
    }
    void set(int i, int n) {
        arr[i] = n;

    }

    void pushback(int n) {
        if (size == cap){
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        int old = arr[size-1];
        size--;
        return old;
    }

    void resize() {

        int * newArr = new int[2*cap];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
        cap = 2*cap;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
        

    }
    private:
        int * arr;
        int cap; 
        int size = 0;
};