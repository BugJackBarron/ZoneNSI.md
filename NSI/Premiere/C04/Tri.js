
t = [12, 18, 1, 56 ,45 ,78, 153, 121, 3]


function triSelection(t){
	let n = t.length;
	for (let i=0; i<n-1; i++){
		let indicemini = i;
		for (let j = i+1; j<n; j++){
			if (t[indicemini]>t[j]){
				indicemini = j;
				}
		}
		let pivot = t[indicemini];
		t[indicemini] = t[i];
		t[i] = pivot;		
	}
	console.log(t);
}

