country={
    "India":"+911",
   "Saudi Arabia":"+966",
   "America":"+199",
   "Europe":"+455",

}
print(country)
for i in country:
    print(i,country[i])
country["Europe"]="+900"
print(country)
