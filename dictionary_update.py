criket={
    'batsman':{
        'rohot': { 'match': 206,
                    'runs' : 100 },

            'virat' : {  'match' : 200,
                         'runs' : 300}

            }}
print(criket)
b=criket.copy();
print(b)
print(b.values())
print(b.keys())
print(b.setdefault(1))
print(b.popitem())
print(b)

