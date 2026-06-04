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
        int * temp = arr;
        cap = cap*2;
        arr = new int[cap];
        for (int i = 0; i < size; i++) {
            arr[i] = temp[i];
        }
        delete[] temp;
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