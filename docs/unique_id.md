# UniqueId Module

## Overview
The `UniqueId` class provides a centralized method for generating UUIDs, ensuring that each instance requiring a unique identifier (e.g., `Task`, `TaskList`) has a consistently unique ID. This class maintains data integrity across the project by preventing manual setting of UUIDs.

## Methods
- **generate_id()**: A static method that uses `uuid4` to generate a unique identifier, returning it as a string.
- **__str__()**: Returns the string representation of `id_value`, allowing it to integrate easily with other classes.

### Design Choices
The `UniqueId` class avoids allowing manual setting of UUIDs to maintain consistent, programmatically generated identifiers. By encapsulating UUID logic, `UniqueId` aligns with the open/closed principle and ensures a single source of truth for ID generation.
