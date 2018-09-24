import {Component, Input, OnInit} from '@angular/core';
import {DataService} from "../data.service";

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

    @Input() dataset_id : number;
    columns : Array<string>;
    rows : Array<Array<string>>;

    constructor(private data : DataService) { }

    ngOnInit() {
        this.data.getRows(this.dataset_id)
            .subscribe(
              res => {this.columns = res['columns']; this.rows = res['rows']},
              error => {console.log(error)}
            );
    }

}
