import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.last_figure = None
        print("Sales Data Analyzer Initialized.")

    def __del__(self):
        print("Prograam close. Resources cleaned.")

    def load_data(self, path):
        try:
            self.data = pd.read_csv(path)
            print("Dataset loaded Successfully!")
        except Exception as e:
            print("Error loading Dataset:", e)

    def explore_data(self):
        if self.data is None:
            print("Load dataset first!")
            return
        
        print("\n== Explore Data ==")
        print("1 Display first 5 rows")
        print("2 Display last 5 rows")
        print("3 Column names")
        print("4 Data types")
        print("5 Basic info")
        print("6 Describe statistics")
        print("7 Search data")
        print("8 Sort data")
        print("9 Filter data")
        
        choice = input("\nEnter your choice: ")
        
        match choice:
            case "1":
                print(self.data.head())
                
            case "2":
                print(self.data.tail())
                
            case "3":
                print(self.data.columns)
                
            case "4":
                print(self.data.dtypes)
                
            case "5":
                self.data.info()
                
            case "6":
                print(self.data.describe())
                
            case "7":
                value = input("Enter value to search: ")
                result = self.data[self.data.astype(str).apply(lambda row: row.str.contains(value, case=False)).any(axis=1)]
                print(result)
                
            case "8":
                col = input("Enter column name: ")
                if col in self.data.columns:
                    print(self.data.sort_values(by=col))
                    
            case "9":
                col = input("Column name: ")
                val = input("Value: ")
                if col in self.data.columns:
                    print(self.data[self.data[col].astype(str) == val])
                    
            case _:
                print("Invalid option.")
                

    def dataframe_operations(self):
        if self.data is None:
            print("Load dataset first!")
            return
        
        print("\n== DataFrame Operations ==")
        print("1 Add Profit Percentage")
        print("2 NumPy operations on Sales")
        print("3 Combine with another dataset")
        print("4 Split dataset by column")
        print("5 Normalize Sales by Region using transform")
        
        choice = input("\nEnter your choice: ")
        
        match choice:
            
            case "1":
                if "Sales" in self.data.columns and "Profit" in self.data.columns:
                    self.data["Profit_Percentage"] = (self.data["Profit"] / self.data["Sales"]) * 100
                    print("Profit percentage column added.")
                    
            case "2":
                if "Sales" in self.data.columns:
                    arr = self.data["Sales"].to_numpy()
                    print("Array:", arr)
                    print("First element:", arr[0])
                    print("First 3 values:", arr[:3])
                    print("Element-wise *2:", arr * 2)
                    
            case "3":
                path = input("Enter second dataset path: ")
                try:
                    df2 = pd.read_csv(path)
                    print("1 Concat")
                    print("2 Merge")
                    c = input("Choice: ")
                    if c == "1":
                        self.data = pd.concat([self.data, df2])
                        print("Datasets combined")
                    elif c == "2":
                        col = input("Merge column: ")
                        self.data = pd.merge(self.data, df2, on=col)
                        print("Datasets merged")
                except Exception as e:
                    print(e)
                    
            case "4":
                col = input("Column to split by: ")
                if col in self.data.columns:
                    groups = self.data.groupby(col)
                    for name, group in groups:
                        print("\nGroup:", name)
                        print(group.head())
                        
            case "5":
                if "Region" in self.data.columns and "Sales" in self.data.columns:
                    self.data["Region_Sales_Normalized"] = self.data.groupby("Region")["Sales"].transform(lambda x: x / x.max())
                    print("Normalized sales column added using transform")
                    print(self.data[["Region","Sales","Region_Sales_Normalized"]].head())                      
            case _:
                print("Invalid option")

    def handle_missing(self):
        if self.data is None:
            print("Load dataset first!")
            return
        print("\n== Handle Missing Data ==")
        print("1 Show missing rows")
        print("2 Fill missing with mean")
        print("3 Drop missing rows")
        print("4 Replace missing with value")
        
        choice = input("\nEnter your Choice: ")
        
        match choice:
            case "1":
                print(self.data[self.data.isnull().any(axis=1)])
                
            case "2":
                self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                
            case "3":
                self.data.dropna(inplace=True)
                
            case "4":
                value = input("Replacement value:")
                self.data.fillna(value, inplace=True)

    def descriptive_stats(self):
        
        if self.data is None:
            print("Load dataset first!")
            return
        
        print(self.data.describe())
        print("STD:\n", self.data.std(numeric_only=True))
        print("VAR:\n", self.data.var(numeric_only=True))
        print("Percentile 90:\n", self.data.quantile(0.9, numeric_only=True))
        print("\nAggregation Example")
        
        for col in self.data.select_dtypes(include=np.number).columns:
            print("\nColumn:", col)
            print("Sum:", self.data[col].sum())
            print("Mean:", self.data[col].mean())
            print("Count:", self.data[col].count())
            
        if "Region" in self.data.columns and "Sales" in self.data.columns:
            print("\nPivot Table")
            pivot = pd.pivot_table(self.data, values="Sales", index="Region", aggfunc="sum")
            print(pivot)

    def visualize(self):
        if self.data is None:
            print("Load dataset first!")
            return
        
        print("\n==Data Visualization==")
        print("1 Bar Plot")
        print("2 Line Plot")
        print("3 Scatter Plot")
        print("4 Pie Chart")
        print("5 Histogram")
        print("6 Stack Plot")
        print("7 Heatmap")
        print("8 Boxplot")
        print("9 Subplots")
        
        choice = input("\nEnter your Choice: ")
        
        match choice:
            
            case "1":
                col = input("Categorical column:")
                self.data[col].value_counts().plot(kind="bar")
                plt.title("Bar Plot")
                
            case "2":
                x = input("X column:")
                y = input("Y column:")
                plt.plot(self.data[x], self.data[y])
                plt.title("Line Plot")
                
            case "3":
                x = input("X:")
                y = input("Y:")
                plt.scatter(self.data[x], self.data[y])
                plt.title("Scatter Plot")
                
            case "4":
                col = input("Column:")
                self.data[col].value_counts().plot(kind="pie", autopct="%1.1f%%")
                plt.title("pie Chart")
                
            case "5":
                col = input("Numeric column:")
                plt.hist(self.data[col])
                plt.title("Histogram")
                
            case "6":
                plt.stackplot(range(len(self.data)), self.data["Sales"], self.data["Profit"], labels=["Sales", "Profit"])
                plt.legend()
                plt.title("stack plot")
                
            case "7":
                sns.heatmap(self.data.corr(numeric_only=True), annot=True)
                plt.title("Heatmap")
                
            case "8":
                col = input("Numeric column:")
                sns.boxplot(y=self.data[col])
                plt.title("Boxplot")
                
            case "9":
                numeric = self.data.select_dtypes(include=np.number)
                fig, ax = plt.subplots(2,2)
                ax[0,0].plot(numeric.iloc[:,0])
                ax[0,1].hist(numeric.iloc[:,0])
                ax[1,0].boxplot(numeric.iloc[:,0])
                ax[1,1].scatter(numeric.iloc[:,0], numeric.iloc[:,1])
                plt.tight_layout()
                
            case _:
                print("Invalid")
        self.last_figure = plt.gcf()
        plt.show()

    def save_visualization(self):
        if self.last_figure is None:
            print("No plot to save")
        else:
            name = input("File name:")
            self.last_figure.savefig(name)

    def menu(self):
        while True:
            print("\n========== Data Analysis & Visualization Program ==========")
            print("1 Load Dataset")
            print("2 Explore Data")
            print("3 Perform DataFrame Operations")
            print("4 Handle Missing Data")
            print("5 Generate Descriptive Statistics")
            print("6 Data Visualization")
            print("7 Save Visualization")
            print("8 Exit")
            print("============================================================")
            choice = input("\nEnter your choice: ")
            match choice:
                case "1":
                    path = input("Dataset path:")
                    self.load_data(path)
                case "2":
                    self.explore_data()
                case "3":
                    self.dataframe_operations()
                case "4":
                    self.handle_missing()
                case "5":
                    self.descriptive_stats()
                case "6":
                    self.visualize()
                case "7":
                    self.save_visualization()
                case "8":
                    print("Exiting the program.Goodbye!")
                    break
                case _:
                    print("Invalid choice")

if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.menu()