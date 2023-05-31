"use client";
// Services can be imported from @/openAPI on Mac/Unix, but Windows cries about this lol
// If this gives you an error, you probably didn't run the 'generate-client', see package.json
import { ItemsService } from "../openAPI/services/ItemsService";

export default function ClientButton() {
  function addItem() {
    //ItemsService.createItem({ name: "item3", price: 5 });
  }
  return <button onClick={() => addItem()}>Add item</button>;
}
