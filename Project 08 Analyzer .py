import numpy as np
class DataAnalysis:

    def __init__(self, array=None):
        self.__array = array

    def __validate(self):
        if self.__array is None:
            print("No array created yet. Please create an array first.")
            return False
        return True

    @classmethod
    def create_array(cls, shape, elements):
        arr = np.array(elements).reshape(shape)
        return cls(arr)

    @staticmethod
    def flatten_array(array):
        return array.flatten()

    def get_array(self):
        return self.__array
 
    def indexing(self, r, c):
        if self.__validate():
            return self.__array[r][c]

    def slicing(self, r_slice, c_slice):
        if self.__validate():
            return self.__array[r_slice, c_slice]

    def combine_vertical(self, other):
        return np.vstack((self.__array, other))

    def combine_horizontal(self, other):
        return np.hstack((self.__array, other))

    def split_array(self, sections):
        return np.array_split(self.__array, sections)

    def add(self, other):
        return self.__array + other

    def subtract(self, other):
        return self.__array - other

    def multiply(self, other):
        return self.__array * other

    def divide(self, other):
        return self.__array / other

    def dot_product(self, other):
        return np.dot(self.__array, other)

    def matrix_multiply(self, other):
        return np.matmul(self.__array, other)

    def search(self, value):
        return np.where(self.__array == value)

    def sort(self, descending=False):
        arr = np.sort(self.__array, axis=1)
        return np.flip(arr, axis=1) if descending else arr

    def filter_condition(self, value):
        return self.__array[self.__array > value]

    def compute_sum(self):
        return np.sum(self.__array)

    def compute_mean(self):
        return np.mean(self.__array)

    def compute_median(self):
        return np.median(self.__array)

    def compute_std(self):
        return np.std(self.__array)

    def compute_variance(self):
        return np.var(self.__array)
    
    #statical functiom
    def minimum(self):
        return np.min(self.__array)

    def maximum(self):
        return np.max(self.__array)

    def percentile(self, p):
        return np.percentile(self.__array, p)

    def correlation(self, other):
        return np.corrcoef(self.__array.flatten(),
                           other.flatten())[0][1]


def main():
    analyzer = None

    print("Welcome to the NumPy Analyzer!")

    while True:

        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":

                print("\nArray Creation:")
                print("Select the type of array to create:")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")

                t = input("Enter your choice: ")

                match t:
                    case "1":
                        size = int(input("Enter number of elements: "))
                        elements = list(map(int, input(f"Enter {size} elements for the array separated by space: ").split()))
                        analyzer = Da.create_array((size,), elements)

                    case "2":
                        r = int(input("Enter the number of rows: "))
                        c = int(input("Enter the number of columns: "))
                        elements = list(map(int, input(f"Enter {r*c} elements for the array separated by space: ").split()))
                        analyzer = DataAnalysis.create_array((r, c), elements)

                    case "3":
                        d1 = int(input("Enter dimension 1: "))
                        d2 = int(input("Enter dimension 2: "))
                        d3 = int(input("Enter dimension 3: "))
                        elements = list(map(int, input(f"Enter {d1*d2*d3} elements separated by space: ").split()))
                        analyzer = DataAnalysis.create_array((d1, d2, d3), elements)

                print("Array created successfully:")
                print(analyzer.get_array())

                print("\nChoose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")

                op = input("Enter your choice: ")

                match op:
                    case "1":
                        r = int(input("Enter row index: "))
                        c = int(input("Enter column index: "))
                        print("Indexed Value:", analyzer.indexing(r, c))

                    case "2":
                        r1, r2 = map(int, input("Enter the row range (start:end): ").split(":"))
                        c1, c2 = map(int, input("Enter the column range (start:end): ").split(":"))
                        print("Sliced Array:")
                        print(analyzer.slicing(slice(r1, r2), slice(c1, c2)))

                    case "3":
                        pass

            case "2":

                if analyzer is None:
                    continue

                print("\nMathematical Operations:")
                print("Choose a mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Dot Product")
                print("6. Matrix Multiplication")

                op = input("Enter your choice: ")

                shape = analyzer.get_array().shape
                elements = list(map(int, input(f"Enter the same-size array elements ({np.prod(shape)} elements separated by space): ").split()))
                other = np.array(elements).reshape(shape)

                print("Original Array:")
                print(analyzer.get_array())
                print("Second Array:")
                print(other)

                match op:
                    case "1":
                        print("Result of Addition:")
                        print(analyzer.add(other))
                    case "2":
                        print("Result of Subtraction:")
                        print(analyzer.subtract(other))
                    case "3":
                        print("Result of Multiplication:")
                        print(analyzer.multiply(other))
                    case "4":
                        print("Result of Division:")
                        print(analyzer.divide(other))
                    case "5":
                        print("Dot Product:")
                        print(analyzer.dot_product(other))
                    case "6":
                        print("Matrix Multiplication:")
                        print(analyzer.matrix_multiply(other))

            case "3":

                if analyzer is None:
                    continue

                print("\nCombine or Split Arrays:")
                print("Choose an option:")
                print("1. Combine Arrays")
                print("2. Split Array")

                op = input("Enter your choice: ")

                match op:
                    case "1":
                        shape = analyzer.get_array().shape
                        elements = list(map(int, input(f"Enter the elements of another array to combine ({np.prod(shape)} elements separated by space): ").split()))
                        other = np.array(elements).reshape(shape)

                        print("Original Array:")
                        print(analyzer.get_array())
                        print("Second Array:")
                        print(other)
                        print("Combined Array (Vertical Stack):")
                        print(analyzer.combine_vertical(other))

                    case "2":
                        sections = int(input("Enter number of sections to split: "))
                        print("Split Result:")
                        print(analyzer.split_array(sections))

            case "4":

                if analyzer is None:
                    continue

                print("\nSearch, Sort, and Filter:")
                print("Choose an option:")
                print("1. Search a value")
                print("2. Sort Ascending")
                print("3. Sort Descending")
                print("4. Filter values")

                op = input("Enter your choice: ")

                match op:
                    case "1":
                        value = int(input("Enter value to search: "))
                        print("Search Result (indices):", analyzer.search(value))

                    case "2":
                        print("Sorted Array:")
                        print(analyzer.sort(False))

                    case "3":
                        print("Sorted Array:")
                        print(analyzer.sort(True))

                    case "4":
                        value = int(input("Filter values greater than: "))
                        print("Filtered Result:")
                        print(analyzer.filter_condition(value))

            case "5":

                if analyzer is None:
                    continue

                print("\nAggregates and Statistics:")
                print("Choose an aggregate/statistical operation:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
                print("6. Minimum")
                print("7. Maximum")
                print("8. Percentile")
                print("9. Correlation")

                op = input("Enter your choice: ")

                match op:
                    case "1":
                        print("Sum of Array:", analyzer.compute_sum())
                    case "2":
                        print("Mean of Array:", analyzer.compute_mean())
                    case "3":
                        print("Median of Array:", analyzer.compute_median())
                    case "4":
                        print("Standard Deviation:", analyzer.compute_std())
                    case "5":
                        print("Variance:", analyzer.compute_variance())
                    case "6":
                        print("Minimum:", analyzer.minimum())
                    case "7":
                        print("Maximum:", analyzer.maximum())
                    case "8":
                        p = float(input("Enter percentile value: "))
                        print("Percentile:", analyzer.percentile(p))
                    case "9":
                        shape = analyzer.get_array().shape
                        elements = list(map(int, input(f"Enter second array elements ({np.prod(shape)} elements separated by space): ").split()))
                        other = np.array(elements).reshape(shape)
                        print("Correlation Coefficient:", analyzer.correlation(other))

            case "6":
                print("Thank you for using the NumPy Analyzer!")
                print("Goodbye!")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
