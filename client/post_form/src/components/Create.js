import React from "react";
import { Form } from 'react-bootstrap';
import { FloatingLabel } from 'react-bootstrap';
import { Button } from 'react-bootstrap';

class Create extends React.Component {


  render() {
    return (
      // title, emotions, body 
      <div>
      <Form>

      <FloatingLabel
    controlId="floatingInput"
    label="Title"
    className="mb-3"
  >
    <Form.Control type="text" placeholder="Title" />
  </FloatingLabel>


  <Form.Select aria-label="Default select example">
  <option>Open this select menu</option>
  <option value="HAPPY">😊 - Feeling Happy</option>
  <option value="SAD">😔 - Feeling Sad</option>
  <option value="ANGRY">😠 - Feeling Angry </option>
  <option value="SURPRISED">😮 - Feeling Surprised</option>
  <option value="CONFUSED">😕 - Feeling Confused</option>
</Form.Select>
<br></br>
<Form.Group>
<FloatingLabel
    controlId="floatingInput"
    label="Body"
    className="mb-3"
  >
 
    
    <Form.Control as="textarea" rows={3} />
    </FloatingLabel>
    </Form.Group>
    <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
      </div>
        
          
        
      
    
    );
  }
}
export default Create;