while getopts ":n:" opt; do
  case ${opt} in
    n )
      echo "The letter picked is : $OPTARG"
      ;;
    \? )
      echo "Invalid option: -$OPTARG" >&2
      ;;
    : )
      echo "Option -$OPTARG requires an argument." >&2
      ;;
  esac
done

