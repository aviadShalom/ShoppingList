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

    this.service.GetShoppingListItem(this.itemID).subscribe( res => {
      if (res == "0"){

      }
      else{
        this.data = res[0];  
      }
      
    })
  }

  openModal(template: TemplateRef<any>) {
    this.modalRef = this.modalService.show(template,Object.assign({}, { class: 'gray modal-lg' }));
  }

  UpdateShoppingListName(){
    this.service.UpdateShoppingListName(this.data.id, this.data.name).subscribe( res => {
      console.log(res);
    })
  }
}
