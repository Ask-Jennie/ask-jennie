import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AskJennieComponent } from './ask-jennie.component';

describe('AskJennieComponent', () => {
  let component: AskJennieComponent;
  let fixture: ComponentFixture<AskJennieComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AskJennieComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AskJennieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
