import { Component, OnInit, TemplateRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ShoppingListService } from './shopping-list.service'
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';
import {  } from '@angular/core';


@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css']
})
export class ShoppingListComponent implements OnInit {
  itemID:string;
  itemsList:any;
  data:any = {id:0,name:"",created:""};
  modalRef: BsModalRef;
  items: any[];
  shoppingItems: any[];

  constructor(private route:ActivatedRoute, private service:ShoppingListService, private modalService: BsModalService) { 
    this.items = Array(15).fill(0);
  }

  ngOnInit() {
    this.itemID = this.route.snapshot.queryParamMap.get('itemID');
    console.log(this.itemID);
    this.service.GetItemsList().subscribe( res => {
      console.log(res);
      this.itemsList = res;
    })
    this.LoadItemList();

    this.service.GetShoppingListItem(this.itemID).subscribe( res => {
      if (res == "0"){

      }
      else{
        this.data = res[0];  
      }
      
    })
  }

  get RefreshList() {
    return this.LoadItemList.bind(this);
  }


  openModal(template: TemplateRef<any>) {
    this.modalRef = this.modalService.show(template,Object.assign({}, { class: 'gray modal-lg' }));
  }

  UpdateShoppingListName(){
    this.service.UpdateShoppingListName(this.data.id, this.data.name).subscribe( res => {
      console.log(res);
    })
  }

  LoadItemList(){
    this.service.GetShoppingListItems(this.itemID).subscribe( res => {
      if (res == "-1" || res == "0"){
        //TODO: error handler
      }
      else{
        this.shoppingItems = res;
      }

    })
  }

  DeleteItemFromList(itemID){
    this.service.DeleteItemFromList(this.itemID, itemID).subscribe( res => {
      if (res == "1"){
        this.LoadItemList();
      }
    })
  }


}
