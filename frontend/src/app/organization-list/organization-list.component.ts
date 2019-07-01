import { Component, OnInit } from '@angular/core';
import { OrganizationService } from '../services/organization.service';

@Component({
  selector: 'app-organization-list',
  templateUrl: './organization-list.component.html',
  styleUrls: ['./organization-list.component.scss']
})

export class OrganizationListComponent implements OnInit {
  organizations = [];

  constructor(private organizationService: OrganizationService) { }

  ngOnInit() {
    this.organizationService.getOrganizations().subscribe((data:  Array<object>) => {
      this.organizations =  data;
    });
  }

}
