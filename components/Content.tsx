// Services can be imported from @/openAPI on Mac/Unix, but Windows cries about this lol
// If this gives you an error, you probably didn't run the 'generate-client', see package.json
import { ItemsService } from "../openAPI/services/ItemsService";

async function getData() {
  const items = await ItemsService.getItems();
  return items.slice(-1)[0].name;
}

export default async function Content() {
  const data = await getData();

  return (
    <span>
      Server sent you a python <span className="text-green-700">{typeof data}</span>: {data}
    </span>
  );
}
