class LinkedList {

    constructor(value){
        this.head = {
            data : value,
            next : null
        };
        this.tail = this.head;
        this.length = 1;
        
    }


    appendNode(value){
        const newNode = {
            data: value,
            next: null
        };
        this.tail.next = newNode;
        this.tail = newNode;
        this.length += 1;
    }


    prependNode(value){
        const preNode = {
            data: value,
            next: null
        };
        preNode.next = this.head;
        this.head = preNode;
        this.length++;
    }

}

//testing the linkedlist
let node1 = new LinkedList(16);
node1.prependNode(5);
node1.prependNode(10);
console.log(node1);
