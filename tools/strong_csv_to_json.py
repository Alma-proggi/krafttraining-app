import csv, json, re, collections
rows=list(csv.DictReader(open('workouts.csv',encoding='utf-8')))
def dur(s):
    h=re.search(r'(\d+)h',s or ''); m=re.search(r'(\d+)min',s or '')
    return (int(h.group(1))*60 if h else 0)+(int(m.group(1)) if m else 0)
W=collections.OrderedDict()
for r in rows:
    d=r['Datum']; wid='w-'+re.sub(r'\D','',d)
    w=W.setdefault(wid,{'date':d.replace(' ','T'),'name':r['Workout-Name'],'durMin':dur(r['Dauer']),'ex':[],'src':'strong'})
    n=r['Name der Übung']
    if not w['ex'] or w['ex'][-1]['n']!=n: w['ex'].append({'n':n,'sets':[],'_rest':[]})
    e=w['ex'][-1]; o=r['Reihenfolge festlegen']
    if o=='Ruhezeit': e['_rest'].append(float(r['Sekunden'] or 0)); continue
    t={'W':'W','D':'D','F':'F'}.get(o,'N')
    s={'t':t,'w':float(r['Gewicht'] or 0),'r':int(float(r['Wiederh.'] or 0))}
    if r.get('RPE'): s['rpe']=float(r['RPE'])
    e['sets'].append(s)
for w in W.values():
    for e in w['ex']:
        rs=e.pop('_rest')
        if rs: e['rest']=int(collections.Counter(rs).most_common(1)[0][0])
json.dump(W,open('workouts.json','w'),ensure_ascii=False)
print(len(W), max(len(json.dumps(w)) for w in W.values()))
print(json.dumps(list(W.values())[-1],ensure_ascii=False)[:600])
# check exercise split by repeated names within workout
print(sum(len(w['ex']) for w in W.values()))
