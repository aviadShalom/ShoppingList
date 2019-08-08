import {Injectable} from '@angular/core';
import {HttpService} from '../core/http.service';
import {Router} from '@angular/router';

@Injectable({
    providedIn:'root'
})

export class ShoppingListService {

    constructor(private httpSrv: HttpService, private router:Router){}

    GetItemsList(){
        return this.httpSrv.post('GetItemsList');
    }

    GetShoppingListItem(itemID){
        return this.httpSrv.post('GetShoppingListItem/'+ itemID);
    }

    UpdateShoppingListName(itemID, name){
        return this.httpSrv.post('UpdateShoppingListName/'+ itemID + "/" + name);
    }
}