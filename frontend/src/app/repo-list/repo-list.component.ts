import { Component, OnInit } from '@angular/core';
import { OrganizationService } from '../services/organization.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-repo-list',
  templateUrl: './repo-list.component.html',
  styleUrls: ['./repo-list.component.scss']
})
export class RepoListComponent implements OnInit {
  repos = [];

  constructor(private route: ActivatedRoute, private organizationService: OrganizationService) {}

  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    this.organizationService.getOrganizationRepos(id).subscribe((data:  Array<object>) => {
      this.repos =  data;
    });
  }

}
