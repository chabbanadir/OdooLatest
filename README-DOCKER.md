# Odoo Docker Compose Setup

This is a Docker Compose project for running Odoo 17 with PostgreSQL database and custom addon support.

## Project Structure

```
.
├── docker-compose.yml      # Docker Compose configuration
├── .env                    # Environment variables
├── config/
│   └── odoo.conf          # Odoo configuration file
├── addons/                # Custom addons directory (initially empty)
└── README-DOCKER.md       # This file
```

## Prerequisites

- Docker and Docker Compose installed
- At least 4GB RAM available
- Port 8069 and 5432 available on your machine

## Quick Start

### 1. Start the Services

```bash
docker-compose up -d
```

The services will start in background mode. This will:
- Start a PostgreSQL database container
- Start an Odoo application container
- Create persistent volumes for data

### 2. Access Odoo

Open your browser and navigate to:
```
http://localhost:8069
```

### 3. Initial Setup

- You'll see the Odoo startup wizard
- Create your first database or use the admin credentials:
  - Master Password: `admin`
  - Database: `odoo`

## Custom Addons

The `addons/` directory is mounted to `/mnt/extra-addons` inside the Odoo container. Any custom modules you create in this directory will be automatically available in Odoo.

### Adding Custom Addons

1. Create your addon module in the `addons/` directory:
```bash
mkdir -p addons/my_custom_module
touch addons/my_custom_module/__init__.py
touch addons/my_custom_module/__manifest__.py
```

2. Restart Odoo to detect new addons:
```bash
docker-compose restart odoo
```

3. Go to Apps in Odoo and update the app list to see your new addon

## Common Commands

### View logs
```bash
docker-compose logs -f odoo
docker-compose logs -f db
```

### Stop services
```bash
docker-compose down
```

### Stop and remove volumes (clean slate)
```bash
docker-compose down -v
```

### Rebuild containers
```bash
docker-compose up -d --build
```

### Access Odoo shell
```bash
docker-compose exec odoo odoo shell
```

### Access database
```bash
docker-compose exec db psql -U odoo -d odoo
```

## Configuration

Edit `config/odoo.conf` to modify Odoo settings:
- Database connection details
- Server ports
- Worker threads
- Custom addons path
- Email configuration
- Logging levels

Edit `.env` file to change environment variables like database credentials or master password.

## Ports

- **Odoo Web Interface**: 8069
- **Odoo Longpolling**: 8072
- **PostgreSQL**: 5432

## Database Details

- **Database Name**: odoo
- **Database User**: odoo
- **Database Password**: odoo
- **Host**: db (inside container)

## Troubleshooting

### Containers won't start
```bash
docker-compose logs
```

### Port already in use
Change the ports in `docker-compose.yml` to use different local ports

### Custom addons not showing
1. Ensure files are in `addons/` directory
2. Restart Odoo: `docker-compose restart odoo`
3. Update app list in Odoo UI

### Database connection errors
Check that the database container is running:
```bash
docker-compose ps
```

## Next Steps

1. Develop your custom addons in the `addons/` directory
2. Test them in Odoo
3. Version control your code using Git
4. Deploy to production using the same Docker setup

## Support

For more information on Odoo development visit:
- [Odoo Documentation](https://www.odoo.com/documentation/)
- [Odoo Developer Documentation](https://www.odoo.com/documentation/17.0/developer.html)
