import pandas as pd
doc = pd.read_csv(r'./posts.csv')

i = 0
while i == 0:
    print("1) Search")
    print("2) Delete")
    print("3) Exit")
    n = int(input())
    match n:
        case 1:
            print("Your searching request")
            search = str(input())
            result = doc.loc[doc['text'].str.contains(search,case=False)]
            result = result.sort_values(by=["created_date"])
            print(result[0:20])
        case 2:
            print("Type ID")
            id = int(input())
            doc.drop([id], axis=0, inplace=True)
            print(doc)
        case 3:
            i = 3
        case default:
            print("What?") 