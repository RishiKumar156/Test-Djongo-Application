// linked-list.model.ts
import { Node } from './node.model';

export class LinkedList {
  head: Node | null = null;

  addNode(data: any): void {
    const newNode = new Node(data);
    if (!this.head) {
      this.head = newNode;
    } else {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = newNode;
    }
  }

  getAllNodes(): Node[] {
    const nodes: Node[] = [];
    let current = this.head;

    while (current) {
      nodes.push(current);
      current = current.next;
    }

    return nodes;
  }
}
