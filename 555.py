import math

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["Relative Closeness (High)"] > arr[j+1]["Relative Closeness (High)"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


acceptedAnswers = []
tHigh = int(input("Time High: "))
tLow = int(input("Time Low: "))

tHigh = tHigh / 1000
tLow = tLow / 1000

commonResistors = [10, 15, 22, 33, 47, 68, 100, 150, 220, 330, 470, 680,  1000, 1500, 2200,  3300, 4700, 6800, 10000, 15000, 22000, 33000,  47000, 68000,  100000, 150000, 220000,  330000, 470000,  680000];
commonCapacitors = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1];

for R1 in commonResistors: # This will run 1000 times
    for R2 in commonResistors: #This will run 1,000,000 times
        for C1 in commonCapacitors: #This will run 10,000,000,000 times
            tC1 = C1 * 0.000001
            print(R1, R2, tC1)
            tHighTemp = 0.693 * (R1 + R2) * tC1;
            tLowTemp = 0.693 *  R2 * tC1;
            if math.isclose(tHighTemp, tHigh, rel_tol=0.1) and math.isclose(tLowTemp, tLow, abs_tol=0.1):
                answer = {
                    "R1": R1,
                    "R2": R2,
                    "C1": str(C1) + "µF",
                    "High": tHighTemp,
                    "Low": tLowTemp,
                    "Relative Closeness (High)": abs(tHighTemp - tHigh) / tHigh,
                    "Relative Closeness (Low)": abs(tLowTemp - tLow) / tLow
                }
                acceptedAnswers.append(answer)
bubbleSort(acceptedAnswers)

fileOut = open("555.csv", "w")
fileOut.write("R1,R2,C1,High,Low,Relative Closeness (High),Relative Closeness (Low)\n")

for answer in acceptedAnswers:

    print(answer)
    fileOut.write(str(answer["R1"]) + "," + str(answer["R2"]) + "," + str(answer["C1"]) + "," + str(answer["High"]) + "," + str(answer["Low"]) + "," + str(answer["Relative Closeness (High)"]) + "," + str(answer["Relative Closeness (Low)"]) + "\n")

fileOut.close()



