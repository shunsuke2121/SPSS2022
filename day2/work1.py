str1 = "stressed"
ans1 = str1[::-1]
print(ans1)
str2 = "パタトクカシーー"
ans2 = str2[0:7:2]
print(ans2)
str3 = "パトカー"
str4 = "タクシー"
ans3 = "".join([i + j for i, j in zip(str3, str4)])
print(ans3)