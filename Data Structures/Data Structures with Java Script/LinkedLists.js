class LinkedList {

    constructor(value){
        this.head = {
            data : value,
            next : null
        }
        this.tail = this.head;
        this.length = 1;
        
    }


    appendNode(value){
        const newNode = new Node(value);
        // const newNode = {
        //     data: value,
        //     next: null
        // };

        this.tail.next = newNode;
        this.tail = newNode;
        this.length += 1;
        return this;
    }


    prependNode(value){
        const preNode = new Node(value);
        // const preNode = {
        //     data: value,
        //     next: null
        // };

        preNode.next = this.head;
        this.head = preNode;
        this.length++;
    }

    insert(index, value){
        if (index >= this.length){
            return this.appendNode(value);
        }

        const insertedNode = new Node(value);
        // const insertedNode = {
        //     data: value,
        //     next: null
        // };

        // [0, 1, 2]
        // nodeA -> insertedNode -> nodeB
        // nodeA = [1]
        const nodeA = this.traverseToIndex(index-1); 
        const nodeB = nodeA.next;

        insertedNode.next = nodeB;
        nodeA.next = insertedNode;

        // nodeA.next = insertedNode;
        // insertedNode.next = nodeA;
        this.length++;


        
        // check if index is 1 to update the head.
        // check if index == this.length to update the tail.
    }

    traverseToIndex(index){
        let steps = 0;
        let currentNode = this.head; // [0]
        while (steps < index){ //1
            currentNode = currentNode.next; //[1]
            steps++;
        }
        return currentNode;
    }

    printList(){
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            // console.log(currentNode.data);
            array.push(currentNode.data);
            currentNode = currentNode.next;
        }
        // return array;
        console.log(array);

    }

    

}


class Node{
    constructor(value){
        this.data = value;
        this.next = null;
    }
}

//testing the linkedlist
const node1 = new LinkedList(1);
// node1.prependNode(0);
node1.appendNode(3);
// node1.appendNode(3);
// console.log(node1);
node1.insert(1, 2);


// node1.prependNode(5);
// node1.prependNode(10);
// console.log(node1);
node1.printList();
