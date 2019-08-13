import { Component, OnInit, Input } from '@angular/core';
import { ShoppingListService } from '../shopping-list/shopping-list.service'
@Component({
  selector: 'app-shopping-item',
  templateUrl: './shopping-item.component.html',
  styleUrls: ['./shopping-item.component.css']
})
export class ShoppingItemComponent implements OnInit {
  @Input() data:any;
  quantity:any = 1;
  @Input() list_id:any;
  @Input() refreshList: Function;

  constructor(private service:ShoppingListService) {
    
   }
  

  ngOnInit() {
    
  }

  AddItem(item_id){
    console.log(this.quantity);
    console.log(item_id);
    console.log(this.list_id);

    this.service.AddItemToList(this.list_id, item_id, this.quantity).subscribe( res => {
      console.log(res);

      this.refreshList();
    })
  }
}
