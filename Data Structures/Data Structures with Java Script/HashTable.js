class HashTable{
    constructor(size){
        this.data = new Array(size);
    }


    set(key, value){
        let address = this._hash(key);
        if(!this.data[address]){
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data
    }


    get(key){
        let address = this._hash(key);
        for(let i = 0; i < this.data[address].length; i++){
            if (this.data[address][i][0] == key){
                return this.data[address][i][1]
            }
        }

    }


    _hash(key){
        let hash = 0;
        for(let i = 0; i < key.length; i++){
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash
    }


    keys(){
        const keys = [];
        for (let i=0; i < this.data.length; i++){
            if(this.data[i]){
                keys.push(this.data[i][0][0]);
            }
        }
        return keys;
    }
}

// Testing Hash table
const myHashTableV2 = new HashTable(5);
console.log(myHashTableV2);
myHashTableV2.set("grapes", 1000);
console.log(myHashTableV2);
myHashTableV2.set("apples", 54);
myHashTableV2.set("oranges", 2);
console.log(myHashTableV2.keys());


// Testing methods used building hashtable 
let abc = ("Name".charCodeAt(1) * 1) % 50;
console.log("Name".charCodeAt(1) % 50)
console.log(String.fromCodePoint(6254));