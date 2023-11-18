import { Component, OnInit } from '@angular/core';
import { LinkedList } from '../data-structure/linkedlist';

@Component({
  selector: 'app-heads',
  templateUrl: './heads.component.html',
  styleUrls: ['./heads.component.scss'],
})
export class HeadsComponent implements OnInit {
  linkedList = new LinkedList();
  constructor() {}
  ngOnInit(): void {
    this.linkedList.addNode({ id: 1, name: 'John' });
    this.linkedList.addNode({ id: 2, name: 'Jane' });
    this.linkedList.addNode({ id: 3, name: 'Doe' });
    this.getAllNodes();
  }
  getAllNodes(): void {
    const allNodes = this.linkedList.getAllNodes();
    console.log('All Nodes:', allNodes);
  }
}
