INSERT about_about_translation (tagline,left_header,left_body,right_header,right_body,master_id,language_code)
SELECT a.tagline,a.left_header,a.left_body,a.right_header,a.right_body,a.id,'en' FROM about_about a;


INSERT people_person_translation (body,master_id,language_code)
SELECT p.body,p.layoutitem_ptr_id,'en' FROM people_person p;