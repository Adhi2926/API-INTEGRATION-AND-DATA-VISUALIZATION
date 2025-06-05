import matplotlib.pyplot as plt

data={
    'sem 1': 9.2,
    'sem 2': 8.9,
    'sem 3': 9.7,
    'sem 4': 8.1,
    'sem 5': 6.6,
    'sem 6': 9.4
}

SEM=list(data.keys());
SPGA=list(data.values());

fig=plt.figure(figsize=(10, 5))
plt.bar(SEM,SPGA, color="blue", width=0.3)
plt.xlabel('sem')
plt.ylabel('sgpa')
plt.title("sem and sgpa")
plt.show()