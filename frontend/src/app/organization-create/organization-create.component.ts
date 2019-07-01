import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { OrganizationService } from '../services/organization.service';

@Component({
  selector: 'app-organization-create',
  templateUrl: './organization-create.component.html',
  styleUrls: ['./organization-create.component.scss']
})

export class OrganizationCreateComponent implements OnInit {
  organizationForm = FormGroup;
  submitted = false;
  success = false;

  constructor(private formBuilder: FormBuilder, private organizationService: OrganizationService) { }

  ngOnInit() {
    this.organizationForm = this.formBuilder.group({
      name: ['', Validators.required],
    });
  }

  onSubmit() {
      this.submitted = true;

      if (this.organizationForm.invalid) {
        return;
      }

      this.organizationService.makeOrganization(this.organizationForm).subscribe(
        (res) => console.log(res),
        (err) => console.log(err)
      );

      this.success = true;
  }

}
