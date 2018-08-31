def best_help(i,w,w_i,v_i,c_i,d,t):
	if (i,w,c_i[i]) in d:
		return d[(i,w,c_i[i])][0]
	if i==-1 or w==0:
		return 0
	elif c_i[i]==0:
		d[(i,w,c_i[i])]=(best_help(i-1,w,w_i,v_i,c_i,d,t),0,(i-1,w,c_i[i-1]))
		return d[(i,w,c_i[i])][0]
	elif w_i[i]>w:
		d[(i,w,c_i[i])]=(best_help(i-1,w,w_i,v_i,c_i,d,t),0,(i-1,w,c_i[i-1]))
		return d[(i,w,c_i[i])][0]
	else:
		k=v_i[i]
		c_i[i]-=1
		l=k+best_help(i,w-w_i[i],w_i,v_i,c_i,d,t)
		k_i=c_i
		c_i[i]+=1
		m=best_help(i-1,w,w_i,v_i,c_i,d,t)
		if l>m:
			d[(i,w,c_i[i])]=(l,1,(i,w-w_i[i],c_i[i]-1))
			t[0]=(i,w,c_i[i])
			return l
		else:
			d[(i,w,c_i[i])]=(m,0,(i-1,w,c_i[i-1]))
			t[0]=(i,w,c_i[i])
			return m

def best(w,l):
	w_i=[]
	v_i=[]
	c_i=[]
	for i in l:
		w_i.append(i[0])
		v_i.append(i[1])
		c_i.append(i[2])
	d={}
	t=[()]
	rr=best_help(len(l)-1,w,w_i,v_i,c_i,d,t)
	key=list(d.keys())[-1]
	res=[0 for i in range(len(l))]
	while True:
		if key not in d:
			break
		v,f,nkey=d[key]
		if f==1:
			res[key[0]]+=1
			key=nkey
		else:
			key=nkey
	return [rr,res]
if __name__=='__main__':
	print(best(3, [(2, 4, 2), (3, 5, 3)]))
	print(best(3, [(1, 5, 2), (1, 5, 3)]))
	print(best(3, [(1, 5, 1), (1, 5, 3)]))
	print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
	print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))