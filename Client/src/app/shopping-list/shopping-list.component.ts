import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ShoppingListService } from './shopping-list.service'

@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css']
})
export class ShoppingListComponent implements OnInit {
  itemID:string;
  itemsList:any;
  constructor(private route:ActivatedRoute, private service:ShoppingListService) { }

  ngOnInit() {
    this.itemID = this.route.snapshot.queryParamMap.get('itemID');
    console.log(this.itemID);
    this.service.GetItemsList().subscribe( res => {
      this.itemsList = res;
    })

    this.service.GetShoppingListItem(this.itemID).subscribe( res => {
      console.log(res);
    })
  }

}
